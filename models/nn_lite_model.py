import os
import numpy as np
import time

import tensorflow as tf
import tflite_runtime.interpreter as tflite

from exe import ploter as JP_P
from exe import checking_function as CF
from exe import csv_writter as CW

#from models import model_input as MI

class NN_TFLITE:
    def __init__(self, config, ckpt_num:int, save_name:str=None, delegate_path:str=None):
        self.config                 = config
        self.ckpt_num               = ckpt_num
        self.delegate_path          = delegate_path

        if save_name != None:
            self.lite_m_s_path = save_name
        else:
            self.lite_m_s_path = "{}/{}/tflite_model-{}_UINT8.tflite".format(self.config.save_info.ckpt_path, self.config.save_info.ckpt_floder, self.ckpt_num)
        
        if CF.check_file(self.lite_m_s_path, False):
            None
        
        ext_delegate = None
        print("model path is : {}".format(self.lite_m_s_path))
        print("delegate path is : {}".format(self.delegate_path))

        if self.delegate_path != None:
            ext_delegate = [tflite.load_delegate(self.delegate_path, {})]
            print("Loading external delegate from {}".format(self.delegate_path))
        else:
            print("Use CPU to inference")

        self.lite_model  = tflite.Interpreter(self.lite_m_s_path, experimental_delegates=ext_delegate)

        self.lite_model.allocate_tensors()

        self.input_info  = self.lite_model.get_input_details()
        self.output_info = self.lite_model.get_output_details()
    
    
    def model_inference(self, feature_array:np.array):
        '''
            This function is used to predict with tf lite model.

            Input:
                feature_array : Numpy array of input feature
            Return:
                inf_res :       Model inference result
        '''
        print("feature_rray")
        print(feature_array)
        res_list = []
        f_shape = feature_array.shape

        inference_time_sum = 0.0

        if len(f_shape) == 2:
            for i in range(0, f_shape[0]):
                tmp_f = feature_array[i, :]
                tmp_f = np.expand_dims(tmp_f, 0)

                self.lite_model.set_tensor(self.input_info[0]['index'], tmp_f)

                clock_initial = time.time()
                self.lite_model.invoke()
                delta = ( time.time() - clock_initial ) * 1000

                tmp_res   = self.lite_model.get_tensor(self.output_info[0]['index'])
                res_list.append(tmp_res[0, :])

                print(f'inference time : {delta:.4f} ms')
        else:
            raise(ValueError("Not yet support single batch"))
        
        inf_res = np.array(res_list)
        
        return inf_res

