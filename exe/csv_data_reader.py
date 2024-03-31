"""
    This function is use to read the csv type data with col
    as different data feature and row as different data record.
"""

from math import ceil

import exe.checking_function as CF

import numpy as np
import pandas as pd
import random


from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

class CSV_data_Formater:
    """
        This class is use to read the data save as csv file.
        Different col should be different data feature and 
        different rol should be different data record. With 
        this class user will able to seperat the training 
        feature and label by the name set for the feature in
        first col. Also create a function to get next batch 
        of data & separate the data as train, test dataset.
    """
    
    def __init__(self, csv_path, feature_name_dict, data_set_dict):
        """
            This function is use to initialize the class
            with user setting.

            Input:
                csv_path: The path to the csv data going to use.
                feature_name_dict: This dict should contain name list 
                    of the first row in csv file which is used to separate 
                    wheather the feature is feature or ground truth label. 
                    key list: [feature, label]
                data_set_dict: This dict should contain setting for
                    create dataset function will separate the data randomly
                    or by assing seed then give a batch of data by function.
                    key list: [test_percent, batch_size, random_seed]
        """

        """ Check csv file exist or not """
        CF.check_file(csv_path)

        """
            Check wheather the key needed to use in the dict input or not.
        """
        CF.check_key_in_dict(feature_name_dict, ["feature", "label"])
        CF.check_key_in_dict(data_set_dict, ["test_percent", "batch_size",
            "random_seed"])

        """
            Store the value into the class variable.
        """
        self.csv_path = csv_path
        self.feature_name_dict = feature_name_dict
        self.data_set_dict = data_set_dict

    def sep_train_test(self):
        """
            This function is use to load the csv data and separate to
            train and test set with user setting ratio and random
            seed. For randomly make random seed set random seed as
            404.

            Input:
                None
            Return:
                None
        """

        """
            Once user set the random seed in data_set_dict to 404, randomly create a new
            random seed.
        """
        if self.data_set_dict["random_seed"] == 404:
            self.data_set_dict["random_seed"] = int(random.random()*100)

            print("User don't set Random seed, will create a random number. :> {}".format(
                self.data_set_dict["random_seed"]
            ))

        """Read the csv file and shuffle the data with random seed"""
        self.all_data = pd.read_csv(self.csv_path)
        self.all_data = shuffle(self.all_data, random_state=self.data_set_dict["random_seed"])

        """
            sSparate the csv data into training and testing set with percentage set in data_set_dict. 
            This separate could be randomly with random seed.
        """
        self.train_data, self.test_data = train_test_split(self.all_data, 
            test_size=self.data_set_dict["test_percent"], random_state=self.data_set_dict["random_seed"])

        """
            Get the numbers of training data and calculate the percentage of user set batch size in training data.
        """
        self.train_data_num = len(self.train_data)

        self.batch_percent  =  self.data_set_dict["batch_size"]/self.train_data_num
        
        """
            Get the number of testing data.
        """
        self.test_data_num  = len(self.test_data)

    def non_separate_data(self, shuffle_bool=True):
        """
            This function is used while once data already seperated.
            Which means the csv only contain trainset or testingset.

            Input:
                None
            Return:
                None
        """

        """
            Read the csv data and shuffle.
        """
        self.all_data = pd.read_csv(self.csv_path)

        if shuffle_bool:
            print("User shuffle data\n")
            self.all_data = shuffle(self.all_data, random_state=self.data_set_dict["random_seed"])
        else:
            None

        """
            The data don't need to separate to training set adn testing set. Set all the data to
            train_data and calculate the number of data.
        """
        self.train_data     = self.all_data
        self.train_data_num = len(self.train_data)
        
        """
            Calculate the percentage of user set batch size in training data.
        """
        if self.data_set_dict["batch_size"] < 1 and self.data_set_dict["batch_size"] > 0:
            self.batch_percent  = self.data_set_dict["batch_size"]
        elif self.data_set_dict["batch_size"] == -1.0:
            print("User want to get all data.")     
            self.batch_percent = 0.99
        else:
            self.batch_percent  = self.data_set_dict["batch_size"]/self.train_data_num

            if self.batch_percent > 1.0:
                print("Avoiding crash set batch ration to 0.99")
                self.batch_percent = 0.99
        
    def get_train_batch(self, num = "None", feature_only=False):
        """
            This function is use to get batch of data from the training set (batch number is set in config).
            Once let the num as default, batch size will be set according to the config file.

            Input:
                num: number of data needed
            Output:
                batch:          List of batch data
                batch_feature:  feature of this batch
                batch_label:    label of this batch 
        """

        """
            Create random seed to get batch data.
        """
        random_seed = int(random.random()*100)

        """
            Once the num is "None" do nothing, otherwise calculate the percentage of batch 
            size.
        """
        if num == "None":
            None
        elif num == -1:
            # print("Direct give all mode.")

            num = self.train_data_num
        else:
            """
                Once the data larger than the total number, set batch number to data number.
            """
            if num > self.train_data_num:
                num = self.train_data_num

            self.batch_percent = num / self.train_data_num


        """
            Once the batch size as the max size. Batch equal to whole data.
        """
        if num == self.train_data_num:
            batch = self.train_data
        else:
            """
                Separate the data to batch and other.
            """
            batch, other = train_test_split(self.train_data, train_size=self.batch_percent, random_state=random_seed)

        """
            Separate the data to feature and label.
        """
        batch_feature = self.get_feature(batch, self.feature_name_dict["feature"])
        if feature_only:
            batch_label = np.zeros((self.train_data_num))
        else:
            batch_label   = self.get_feature(batch, self.feature_name_dict["label"])


        return batch, batch_feature, batch_label

    def get_test_batch(self, num):
        """
            This function is use to get testing data batch as feature and label.

            Input:
                num: number of data needed
            Output:
                batch_feature:  feature of this batch
                batch_label:    label of this batch 
        """

        """
            Create random seed to get batch data.
        """
        random_seed = int(random.random()*100)

        """
            Once the data larger than the total number, set batch number to data number.
        """
        if num > self.test_data_num:
            num = self.test_data_num
        
        """        
            Calculate the percentage of batch size user want to get.
        """
        percent     = num / self.test_data_num

        """
            Once the batch size as the max size. Batch equal to whole data.
        """
        if num == self.test_data_num:
            batch = self.test_data
        else:
            """
                Separate the data to batch and other.
            """
            other, batch = train_test_split(self.test_data, test_size=percent, random_state=random_seed)

        """
            Separate the data to feature and label.
        """
        batch_feature = self.get_feature(batch, self.feature_name_dict["feature"])
        batch_label   = self.get_feature(batch, self.feature_name_dict["label"])

        return batch_feature, batch_label

    def get_feature(self, data, feature):
        """
            This function is use to get the specific col from file data.

            Input:
                data: Data read by pd.
                feature: The column key ""list"" which is needed.
            Return:
                res_frame: The specific column.
        """

        """
            Set the index to zero. 
            Set the data numbers as count.
            Set tar_size as the number of features
        """
        index = 0
        count = data.shape[0]
        tar_size = len(feature)

        """
            Create an zero array to save the result.
        """
        tar = np.zeros([count, tar_size])

        """
            Assign value match user want to get into the tar array.
        """
        for col in feature:
            tar[:, index] = data[col]
            index += 1

        """
            Make the tar array to pd format.
        """
        res_frame = pd.DataFrame({feature[0]: tar[:,0]})

        for i in range(1, tar_size):
            
            new_frame = pd.DataFrame({feature[i]: tar[:, i]}) 
            res_frame = res_frame.join(new_frame)

        #print(res_frame)
        return res_frame
    
