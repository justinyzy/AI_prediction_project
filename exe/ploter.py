import matplotlib.pyplot as plt
from numpy import save

import exe.checking_function as CF

class JP_plotter:
    def __init__(self):

        self.default_color = ["b", "r", "g", "c", "m", "y", "k"]
        self.default_type = [".", "-", "o"]
            
    def plot_2d(self, x_list, y_list, info_dict = {"title": "Non", "x_label": "x", "y_label": "y"}, 
        show_b=True, hold_bool=False, color_list=None, type_list=None, legend_list=[], save_dict={"save_b": False,
        "save_p": ".", "save_n": "test"}):
        """
            This function is used to plot the x and y 2D plot. 
            This funciton is able to plot multi result on the same figure.

            Input:
                x_list: x data need to be plot on the figure.
                y_list: y data need to be plot on the figure.
                info_dict: Dict setting for title, label name. Should contain keys: [title, x_label, y_label]
                show_b: Wheather to create window
                hold_bool: Wheather user want to  hold after this plot.
                color_list: Color list correspond to different data (optional) [Able to auto repeat]. 
                type_list: Type list correspond to different data (optional) [Able to auto repeat].
                save_dict: Dict save for saving data
            Return:
                None
        """

        CF.check_key_in_dict(info_dict, ["title", "x_label", "y_label"])

        fig, ax = plt.subplots()
        for i in range(0, len(x_list)):
            x_this = x_list[i]
            y_this = y_list[i]

            if color_list != None:
                color_this = color_list[i%len(color_list)]
            else:
                color_this = self.default_color[i%len(self.default_color)]

            if type_list != None:
                type_this = type_list[i%len(type_list)]
            else:
                type_this = self.default_type[i%len(self.default_type)]

            plt.plot(x_this, y_this, color_this+type_this)

        plt.title(info_dict["title"])
        plt.xlabel(info_dict["x_label"])
        plt.ylabel(info_dict["y_label"])
        plt.legend(legend_list)

        plt.grid()

        if show_b:
            plt.show(block=hold_bool)
        
        if save_dict["save_b"]:
            # CF.check_dir_exist(save_dict["save_p"])

            #plt.savefig("{}{}.jpg".format(save_dict["save_p"], save_dict["save_n"]))
            plt.savefig("{}{}.png".format(save_dict["save_p"], save_dict["save_n"]), dpi=300)


    
    def plot_info_list(self, time, feature, same_type=None, same_color=None):
        """
            Use to create needed for plot_2d when user want to create for multi dim
            feature. [15, 4] -> [[15, 1], [15, 1], [15, 1],[15, 1]]

            Input:
                time:
                feature:
                same_type:
                same_color:
            Return:
                res_time_list:
                res_feature_list:
                res_type_list:
                res_color_list:
        """

        res_time_list = []
        res_type_list = []
        res_color_list = []
        res_feature_list = []

        for i in range(0, feature.shape[1]):
            res_time_list.append(time)
            res_feature_list.append(feature[:, i])

            if same_color != None:
                res_color_list.append(same_color)
            else:
                res_color_list.append(self.default_color[i%len(self.default_color)])

            if same_type != None:
                res_type_list.append(same_type)
            else:
                res_type_list.append(self.default_type[i%len(self.default_type)])                

        return res_time_list, res_feature_list, res_type_list, res_color_list


