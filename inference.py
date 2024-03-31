import os
import numpy as np
import time
import pandas as pd

import tensorflow as tf

from absl import app
from absl import flags
from shutil import copyfile

from exe import checking_function as CF
from exe import config_reader as CR
from exe import csv_writter as CW
from exe import ploter as JP_P

from models import nn_lite_model as NN_Lite
from functools import partial
import server
import pickle

FLAGS = flags.FLAGS
flags.DEFINE_string("config_record_p", "config_record.config", "Config record saved while model training")
flags.DEFINE_integer("last_end_ckpt", 10000, "The steps of saved file to be reused")
flags.DEFINE_string("Save_dir", "./99_model_record/Inference_Result", "Directory to save the reloading inference result")
flags.DEFINE_string("Save_name", "Inference_testing_set_result", "Directory to save the result should not contain .csv, set as None to disable saving function")
flags.DEFINE_string("delegate_p", "", "External delegate library path")

def main(args,data_in,client_socket):
    
    user_config = CR.config_reader("JP_NN_proto", FLAGS.config_record_p)["JP_NN_proto"].nn_hd_info

    if FLAGS.delegate_p == "":
        JP_NN_LITE = NN_Lite.NN_TFLITE(user_config, FLAGS.last_end_ckpt, None)
    else:
        JP_NN_LITE = NN_Lite.NN_TFLITE(user_config, FLAGS.last_end_ckpt, None, FLAGS.delegate_p)
    
    #batch_f = [[3.012946,1.722745,3.545604,2.425639,0.990154,0.588558,0.174714]]
    
    row = int((len(data_in))/7)

    for i in range(row):
        batch_f = data_in.iloc[:7].values.reshape((1,7))  ##存成np array 並且reshape
        data_in = data_in.drop(index=data_in.index[:7])  ##刪除資料前7項
        batch_f = np.float32(batch_f)
        print("batch "+str(int(i+1)))
        print("batch_f (temperature delta)")
        print(batch_f)
        inf_res = JP_NN_LITE.model_inference(batch_f)

        print("thermal expansion "+str(int(i+1)))
        print("inf_res (predicted thermal expansion error)")
        print(inf_res)

        server.send_data(client_socket,inf_res)

        print("-----END-----")
        print("Send data to Client.")
        print("")

if __name__ == "__main__":
    data = pd.read_csv("result.csv")  #### read csv as dataframe
    print("Load data sucess.")
    print(data)
    server_socket,client_socket=server.connect_server()
    partial_main = partial(main, data_in=data,client_socket=client_socket)

    app.run(partial_main)
    server.close_connect(server_socket,client_socket)
