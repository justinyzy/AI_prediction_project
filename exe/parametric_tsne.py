import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tqdm import tqdm
import numpy as np
import numba

import sklearn
from sklearn.base import BaseEstimator, TransformerMixin

# import keras.backend as K
# from keras.models import Sequential
# from keras.layers import Dense, InputLayer, Dropout
# from keras.callbacks import TensorBoard
# from keras.optimizers import Adam

import tensorflow.keras.backend as K
# from tensorflow.python.keras import backend as K
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense, InputLayer, Dropout

import tensorflow as tf

tf.compat.v1.disable_eager_execution()

@numba.jit(nopython=True, error_model='numpy')          # https://github.com/numba/numba/issues/4360
def Hbeta(D, beta):

    P = np.exp(-D * beta)
    sumP = np.sum(P)                                    # ACHTUNG! This could be zero!
    H = np.log(sumP) + beta * np.sum(D * P) / sumP      # ACHTUNG! Divide-by-zero possible here!
    P = P / sumP                                        # ACHTUNG! Divide-by-zero possible here!
    
    return H, P

@numba.jit(nopython=True)
def x2p_job(data, max_iteration=50, tol=1e-5):
    i, Di, logU = data
    
    beta = 1.0
    beta_min = -np.inf
    beta_max = np.inf
    
    H, thisP = Hbeta(Di, beta)
    Hdiff = H - logU

    tries = 0
    while tries < max_iteration and np.abs(Hdiff) > tol:
    
        # If not, increase or decrease precision
        if Hdiff > 0:
            beta_min = beta
            if np.isinf(beta_max):      # Numba compatibility: isposinf --> isinf
                beta *= 2.
            else:
                beta = (beta + beta_max) / 2.
        else:
            beta_max = beta
            if np.isinf(beta_min):      # Numba compatibility: isneginf --> isinf
                beta /= 2. 
            else:
                beta = (beta + beta_min) / 2.

        H, thisP = Hbeta(Di, beta)
        Hdiff = H - logU
        tries += 1

    return i, thisP

def x2p(X, perplexity, n_jobs=None):

    n = X.shape[0]
    logU = np.log(perplexity)

    sum_X = np.sum(np.square(X), axis=1)
    D = sum_X + (sum_X.reshape((-1, 1)) - 2 * np.dot(X, X.T))

    idx = (1 - np.eye(n)).astype(bool)
    D = D[idx].reshape((n, -1))

    P = np.zeros([n, n])
    for i in range(n):
        P[i, idx[i]] = x2p_job((i,D[i],logU))[1]

    return P

def write_log(callback, names, logs, batch_no):
    for name, value in zip(names, logs):
        summary = tf.compat.v1.Summary()
        summary_value = summary.value.add()
        summary_value.simple_value = value
        summary_value.tag = name
        callback.writer.add_summary(summary, batch_no)
        callback.writer.flush()


class ParametricTSNE(BaseEstimator, TransformerMixin):

    def __init__(self, n_components=2, perplexity=30.,
                n_iter=1000,
                batch_size=500,
                early_exaggeration_epochs = 50,
                early_exaggeration_value = 4.,
                early_stopping_epochs = np.inf,
                early_stopping_min_improvement = 1e-2,
                alpha = 1,
                nl1 = 1000,
                nl2 = 500,
                nl3 = 250,
                logdir=None, verbose=0, var_smooth_coef=0.0, leaky_bool=False, GPU_CODE="0", GPU_FRAC=0.1):
        
        gpu_opt     = tf.compat.v1.GPUOptions(visible_device_list=GPU_CODE,
            per_process_gpu_memory_fraction=GPU_FRAC)
        sess_config = tf.compat.v1.ConfigProto(gpu_options=gpu_opt)

        self.sess = tf.compat.v1.Session(config=sess_config)
        tf.compat.v1.keras.backend.set_session(self.sess)

        self.n_components = n_components
        self.perplexity = perplexity
        self.n_iter = n_iter
        self.batch_size = batch_size
        self.verbose = verbose
        self.smooth_var_coef = var_smooth_coef
        self.leaky_bool = leaky_bool

        # FFNet architecture
        self.nl1 = nl1
        self.nl2 = nl2
        self.nl3 = nl3

        # Early-exaggeration
        self.early_exaggeration_epochs = early_exaggeration_epochs
        self.early_exaggeration_value = early_exaggeration_value
        # Early-stopping
        self.early_stopping_epochs = early_stopping_epochs
        self.early_stopping_min_improvement = early_stopping_min_improvement

        # t-Student params
        self.alpha = alpha

        # Tensorboard
        self.logdir = logdir

        # Internals
        self._model = None
        
    def fit(self, X, y=None):

        self.sess.run(tf.compat.v1.global_variables_initializer())

        """fit the model with X"""
        
        if self.batch_size is None:
            self.batch_size = X.shape[0]
        else:
            # HACK! REDUCE 'X' TO MAKE IT MULTIPLE OF BATCH_SIZE!
            m = X.shape[0] % self.batch_size
            if m > 0:
                X = X[:-m]
            
            if y is None:
                None
            else:
                rem = y.shape[0] % self.batch_size
                if rem > 0:
                    y = y[:-rem]

        n_sample, n_feature = X.shape

        self._log('Building model..', end=' ')
        self._build_model(n_feature, self.n_components)
        self._log('Done')

        self._log('Start training..')
        
        # Tensorboard
        if not self.logdir == None:
            # callback = TensorBoard(self.logdir)
            # callback = tf.keras.callbacks.TensorBoard(self.logdir)
            # callback.set_model(self._model)
            callback = None
        else:
            callback = None

        # Early stopping
        es_patience = self.early_stopping_epochs
        es_loss = np.inf
        es_stop = False

        # Precompute P (once for all!)
        if y is None:
            print("DB parametric_tsne.py L175 >> y == none. Calculate P with X")
            P = self._calculate_P(X)                
        else:
            print("DB parametric_tsne.py L178 >> y != none. Calculate P with y")
            P = self._calculate_P(y)

        epoch = 0
        while epoch < self.n_iter and not es_stop:

            # Make copy
            _P = P.copy()

            ## Shuffle entries
            # p_idxs = np.random.permutation(self.batch_size)
    
            # Early exaggeration        
            if epoch < self.early_exaggeration_epochs:
                _P *= self.early_exaggeration_value

            # Actual training
            loss = 0.0
            n_batches = 0
            for i in range(0, n_sample, self.batch_size):
                
                batch_slice = slice(i, i + self.batch_size)
                X_batch, _P_batch = X[batch_slice], _P[batch_slice]
                
                # Shuffle entries
                p_idxs = np.random.permutation(self.batch_size)
                # Shuffle data
                X_batch = X_batch[p_idxs]
                # Shuffle rows and cols of P
                _P_batch = _P_batch[p_idxs, :]
                _P_batch = _P_batch[:, p_idxs]

                loss += self._model.train_on_batch(X_batch, _P_batch)
                n_batches += 1
            
            # End-of-epoch: summarize
            loss /= n_batches

            if epoch % 10 == 0:
                self._log('Epoch: {0} - Loss: {1:.3f}'.format(epoch, loss))
            
            if callback is not None:
                # Write log
                write_log(callback, ['loss'], [loss], epoch)

            # Check early-stopping condition
            if loss < es_loss and np.abs(loss - es_loss) > self.early_stopping_min_improvement:
                es_loss = loss
                es_patience = self.early_stopping_epochs
            else:
                es_patience -= 1

            if es_patience == 0:
                self._log('Early stopping!')
                es_stop = True

            # Going to the next iteration...
            del _P    
            epoch += 1

        self._log('Done')

        # Save the model
        self._model.save(self.logdir)

        return self  # scikit-learn does so..
        
    def transform(self, X):
        """apply dimensionality reduction to X"""
        # fit should have been called before
        if self.model is None:
            raise sklearn.exceptions.NotFittedError(
                'This ParametricTSNE instance is not fitted yet. Call \'fit\''
                ' with appropriate arguments before using this method.')

        # self._log('Predicting embedding points..', end=' ')
        X_new = self.model.predict(X, batch_size=X.shape[0])

        # self._log('Done')

        return X_new

    def fit_transform(self, X, y=None):


        """fit the model with X and apply the dimensionality reduction on X."""
        self.fit(X, y)

        X_new = self.transform(X)
        return X_new

    # ================================ Internals ================================

    def _calculate_P(self, X):
        n = X.shape[0]
        P = np.zeros([n, self.batch_size])
        self._log("Computing P...")
        for i in tqdm(np.arange(0, n, self.batch_size)):
            P_batch = x2p(X[i:i + self.batch_size], self.perplexity)
            P_batch[np.isnan(P_batch)] = 0
            P_batch = P_batch + P_batch.T
            P_batch = P_batch / P_batch.sum()
            P_batch = np.maximum(P_batch, 1e-12)
            P[i:i + self.batch_size] = P_batch
        return P

    def _kl_divergence(self, P, Y):
        sum_Y = K.sum(K.square(Y), axis=1)
        eps = K.variable(1e-15)
        D = sum_Y + K.reshape(sum_Y, [-1, 1]) - 2 * K.dot(Y, K.transpose(Y))
        Q = K.pow(1 + D / self.alpha, -(self.alpha + 1) / 2)
        Q *= K.variable(1 - np.eye(self.batch_size))
        Q /= K.sum(Q)
        Q = K.maximum(Q, eps)
        C = K.log((P + eps) / (Q + eps))
        C = K.sum(P * C)

        # C = C + self.smooth_var_coef * self._cal_noise_effect(P)

        return C

    def _cal_noise_effect(self, data):
        fft_list = []
        score = 0
        data = tf.cast(data, tf.complex64)

        for men in range(0, self.n_components):
            # fft_res = np.fft.fft(data[:, men])
            fft_res = tf.signal.fft(data[:, men])
            fft_res = tf.abs(tf.multiply(fft_res,  1/self.batch_size))
            fft_res = fft_res[5:int((self.batch_size-1)/2)]
            normalize_show_fft = (fft_res-tf.reduce_min(fft_res)) / (tf.reduce_max(fft_res) - tf.reduce_min(fft_res))

            fft_list.append(tf.clip_by_value(normalize_show_fft, 0.0, 0.05))

        score = tf.reduce_sum(fft_list)

        return score

    def _build_model(self, n_input, n_output):
        self._model = Sequential()
        self._model.add(InputLayer((n_input,)))
        # Layer adding loop
        for n in [self.nl1, self.nl2, self.nl3]:
            if self.leaky_bool:
                self._model.add(Dense(n, activation=tf.nn.leaky_relu))
            else:
                self._model.add(Dense(n, activation='relu'))
        self._model.add(Dense(n_output, activation='linear'))
        self._model.compile('adam', self._kl_divergence)

    def _log(self, *args, **kwargs):
        """logging with given arguments and keyword arguments"""
        if self.verbose >= 1:
            print(*args, **kwargs)

    @property
    def model(self):
        return self._model

class KL_divergence(tf.keras.layers.Layer):
    """
        This class is used to save the ptsne in joblib
    """

    def __init__(self):
        print("Init KL divergence custom objects")

    def call(self, P, Y):
        sum_Y = K.sum(K.square(Y), axis=1)
        eps = K.variable(1e-15)
        D = sum_Y + K.reshape(sum_Y, [-1, 1]) - 2 * K.dot(Y, K.transpose(Y))
        Q = K.pow(1 + D / 10.0, -(10.0 + 1) / 2)
        Q *= K.variable(1 - np.eye(10))
        Q /= K.sum(Q)
        Q = K.maximum(Q, eps)
        C = K.log((P + eps) / (Q + eps))
        C = K.sum(P * C)    
    
def _kl_divergence(P, Y):
    sum_Y = K.sum(K.square(Y), axis=1)
    eps = K.variable(1e-15)
    D = sum_Y + K.reshape(sum_Y, [-1, 1]) - 2 * K.dot(Y, K.transpose(Y))
    Q = K.pow(1 + D / 10.0, -(10.0 + 1) / 2)
    Q *= K.variable(1 - np.eye(10))
    Q /= K.sum(Q)
    Q = K.maximum(Q, eps)
    C = K.log((P + eps) / (Q + eps))
    C = K.sum(P * C)

    # C = C + self.smooth_var_coef * K.mean(K.var(P, 0))

    return C