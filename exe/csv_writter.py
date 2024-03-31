import os
import csv
import numpy as np
import exe.checking_function as CF

class JP_CSV_Writter:
    def __init__(self, data:np.array, header:list, save_dir:str, file_name:str):
        """
            This function is used to save the np array in to a csv file

            Input:
                data:       Numpy array with shape: [batch, columns].
                header:     Header of the csv file.
                save_dir:   Dir to save the file.
                file_name:  Name of the file.
            Return:
                None
        """

        self.file_p = "{}/{}.csv".format(save_dir, file_name)
        
        s_ch = self.check_data_shape(data, header)
        p_ch = CF.check_dir_exist(save_dir, True, False)
        f_ch = CF.check_file(self.file_p, False)

        if f_ch:
            user_set = input("File already exis!! Enter 1 to force write:\t")

            if user_set == str(1):
                None
            else:
                raise(ValueError("Break to protect the file.....\n"))

        self.save_the_file(data, header, self.file_p)

    def check_data_shape(self, data:np.array, header:list):
        """
            This function is used to check the shape of data is fine to be save with 
            this function, which should be [batch_size, n_features].

            Input: 
                data: numpy array of data.
                header: Header to save the csv
            Return:
                res: Boolean of the check result.
        """

        d_s = data.shape

        if len(d_s) != 2:
            warm_info = "Data shape Error!!! Should be [batch_size, n_features] but get: {}".format(d_s)
            raise(ValueError(warm_info))
        else:
            len_check = True

        
        if len(header) == d_s[1]:
            f_l_check = True
        else:
            # if self.time_stamp_b:
            #     if len(header) -1 == d_s[1]:
            #         f_l_check = True
            # else:
            warm_info = "Header length != feature numbers ({} & {})".format(len(header), d_s[1])
            raise(ValueError(warm_info))
        
        res = len_check and f_l_check

        return res

    def try_open_csv(self, path:str):
        """
            Repeat try until open an csv file that are writeable.

            Input:
                path: file path to open.
            Return:
                csv_file: open csv file with os function.
        """

        while 1:
            try:
                csv_file = open(path, "w", newline="")
                if csv_file.writable:
                    break
                else:
                    print("CSV non writeable, try reopening....")
            except Exception as e:
                print("Error opening csv file: {}".format(e))
            
        return csv_file

    def save_the_file(self, data:np.array, header:list, file_p:str):
        """
            This function will open a csv file and save the result

            Input:
                data: array to save
                header: Header of csv file
                file_p: path of the csv should contain .csv
            Return:
                None
        """
        d_s      = data.shape
        csv_file = self.try_open_csv(file_p)

        writter  = csv.writer(csv_file)
        writter.writerow(header)

        for i in range(0, d_s[0]):
            # if self.time_stamp_b:
            #     time_stamp = list(i)
            #     writter.writerow(time_stamp.append(list(data[i, :])))
            # else:
            writter.writerow(list(data[i, :]))

        csv_file.close()


def try_open_csv(path:str):
    """
        Repeat try until open an csv file that are writeable.

        Input:
            path: file path to open.
        Return:
            csv_file: open csv file with os function.
    """

    while 1:
        try:
            csv_file = open(path, "w", newline="")
            if csv_file.writable:
                break
            else:
                print("CSV non writeable, try reopening....")
        except Exception as e:
            print("Error opening csv file: {}".format(e))
        
    return csv_file

def save_the_file(data:np.array, header:list, file_p:str):
    """
        This function will open a csv file and save the result

        Input:
            data: array to save
            header: Header of csv file
            file_p: path of the csv should contain .csv
        Return:
            None
    """
    d_s      = data.shape
    csv_file = try_open_csv(file_p)

    writter  = csv.writer(csv_file)
    writter.writerow(header)

    for i in range(0, d_s[0]):
        # if self.time_stamp_b:
        #     time_stamp = list(i)
        #     writter.writerow(time_stamp.append(list(data[i, :])))
        # else:
        writter.writerow(list(data[i, :]))

    csv_file.close()


