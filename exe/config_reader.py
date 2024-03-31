"""Fuctions for reading configuration files"""
import os
import tensorflow as tf

from google.protobuf import text_format

from protos import SVR_h_d_pb2
from protos import bayesian_mixing_pb2
from protos import nn_regression_pb2
from protos import bay_compare_pb2
from protos import spindle_bay_reporter_pb2
from protos import bay_nn_model_pb2
from protos import data_offseter_pb2

import exe.checking_function as CF

"""
    This dict is use to set the proto able to read.
"""
proto_dict = {
    "JP_SVR_proto":   SVR_h_d_pb2.MAIN(),
    "JP_BAY_SVR"  :   bayesian_mixing_pb2.MAIN_bay(),
    "JP_NN_proto": nn_regression_pb2.MAIN_NN_R(),
    "bay_compare": bay_compare_pb2.MAIN_bay_com(),
    "Spindle_bay_report": spindle_bay_reporter_pb2.Spindle_bay_report(),
    "JP_BYA_NN": bay_nn_model_pb2.Main_bay_NN(),
    "JP_data_offseter": data_offseter_pb2.Mina_Data_offseter()
}

def config_reader(proto_type, config_path="../configs/env_test.config"):
    """
        Read model config file.

        Args:
            proto type: The type user want to read. Need to exist in the proto dict.
            model_config_path: Path to the config file match the proto file.
        
        Returns:
            Dictionary of configuration objects. Keys are `model`
    """

    """
        Create dict to save the result
    """
    configs = {}


    """
        Check the config file exist or not.
    """
    check_file = CF.check_file(config_path)

    
    if check_file:
        
        """
            Assign key for saving the result.
        """
        pb2_file = proto_dict[proto_type]

        """
            Read the config file and decode with the protobuf format. 
        """
        with tf.io.gfile.GFile(config_path, "r") as f:
            text_format.Merge(f.read(), pb2_file)
            configs[proto_type] = pb2_file

    return configs



    