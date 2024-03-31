import os
import csv
import numpy as np

from exe import checking_function   as CF
from exe import csv_data_reader     as CDR
from exe import csv_writter         as CW
from exe import ploter              as JP_P

class Data_offseter:
    """
        This function is used to apply init offset or env offset.
    """

    def __init__(self, user_config):
        """
            Input:
                user_config: Config following data_offseter.proto.
            Return:
                None
        """

        self.user_config = user_config.data_offseter
        self.save_info   = self.user_config.save_info
        self.offset_info = self.user_config.offset_info
    
        print("User config: \n{}".format(self.user_config))

    def exe(self):
        """
            Applying data_offseter with user config.

            Input:
                None
            Return:
                None
        """

        CF.check_file(self.user_config.target_csv_file)

        feature_dict = {
            "feature": self.user_config.target_f_list,
            "label": "time"
        }

        data_set_dict = {
            "test_percent": 0, 
            "batch_size": -1, 
            "random_seed": 1
        }

        self.data_reader = CDR.CSV_data_Formater(self.user_config.target_csv_file,
            feature_dict, data_set_dict)
        
        self.data_reader.non_separate_data(False)

        if self.user_config.offset_info.HasField("init_offset_info"):
            offset_data_frame = self.init_offseter(self.data_reader.all_data)
        elif self.user_config.offset_info.HasField("feature_offset_info"):
            offset_data_frame = self.feature_offseter(self.data_reader.all_data)
        else:
            raise(ValueError("Unknown user select offset method...."))

        save_path = '{}/{}.csv'.format(self.save_info.save_dir, self.save_info.save_name)

        over_c = CF.check_file(save_path, False)
        if over_c:
            user_input = input("Data already exist... -> Enter 1 to force write")

            if user_input == "1":
                None
            else:
                raise(ValueError("Break to protect the file....."))

        offset_data_frame.to_csv(save_path, index=False)

        if self.save_info.save_img_b:
            print("Unfinish feature...")

    def feature_offseter(self, csv_data_frame):
        """
            This function is used to apply feature offset to the assign feature
            with assigning target and index.

            Input:
                csv_data_frame: All data from the data reader.
            Return:
                res_data_frame: Data frame merge with new offset feature.
        """
        res_data_frame = csv_data_frame
        f_offset_info = self.offset_info.feature_offset_info

        target_f = self.data_reader.get_feature(csv_data_frame, self.user_config.target_f_list)
        f_target = self.data_reader.get_feature(csv_data_frame, f_offset_info.tar_f_list)

        for f_ind in range(0, target_f.shape[1]):
            tmp_this_key = "{}_{}".format(self.user_config.target_f_list[f_ind], 
                self.user_config.s_tail_list[f_ind])
            
            tmp_this_f = target_f[:, f_ind] - f_target[:, f_ind]

            res_data_frame[tmp_this_key] = tmp_this_f

        return res_data_frame

    def init_offseter(self, csv_data_frame):
        """
            This function is used to apply init offset to the assign feature
            with assigning target and index.

            Input:
                csv_data_frame: All data from the data reader.
            Return:
                res_data_frame: Data frame merge with new offset feature.
        """
        res_data_frame = csv_data_frame
        init_offset_info = self.offset_info.init_offset_info

        target_f = self.data_reader.get_feature(csv_data_frame, self.user_config.target_f_list).values
        init_target = self.data_reader.get_feature(csv_data_frame, init_offset_info.tar_f_list).values

        ind_list = list(init_offset_info.init_index_list)
        ind_list.append(target_f.shape[0])
        
        for f_ind in range(0, target_f.shape[1]):

            tmp_this_key = "{}_{}".format(self.user_config.target_f_list[f_ind], 
                self.user_config.s_tail_list[f_ind])
            
            tmp_this_f = np.zeros(target_f.shape[0])

            for i in range(0, len(ind_list) - 1):
                section_tar = init_target[ind_list[i], f_ind]

                s_ind = ind_list[i]
                if i != len(ind_list) - 2:
                    e_ind = ind_list[i+1]-1
                else:
                    e_ind = ind_list[i+1]

                print("s_ind: {} -> end_ind: {}".format(s_ind, e_ind))

                tmp_f = target_f[s_ind:e_ind, f_ind]
                res_f = tmp_f - section_tar

                tmp_this_f[s_ind:e_ind] = res_f

            res_data_frame[tmp_this_key] = tmp_this_f
            # res_list.append(tmp_this_f)

        return res_data_frame



        


            
                


                













                











        