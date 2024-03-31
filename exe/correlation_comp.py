import numpy as np
import math

import exe.checking_function as CF
import exe.ploter as JP_P

from scipy import stats

class Correlation_comp:
    def __init__(self, data_dict, info_dict):
        """
            This function is used to compare correlations between
            different data.

            Input:
                data_dict: Should contain keys [tar_data, comp_data_list]
                info_dict: Should contain keys [method_list, data_name_list]
            Return:
                None
        """

        CF.check_key_in_dict(data_dict, ["tar_data", "comp_data_list"])
        CF.check_key_in_dict(info_dict, ["method_list", "data_name_list", "data_set_name"])

        self.mov_win_size = math.ceil(data_dict["tar_data"].shape[0]/100)

        self.data_dict = data_dict
        self.info_dict = info_dict

        print("User want to compare correlation of: {}".format(info_dict))
        print("Mov window size: {}".format(self.mov_win_size))
    
    def exe(self, show_b=False, save_p="../100_DB"):
        """
            This function is used to operate the compare between different 
            data. The correlation method only support pearson's and 
            speerman's now.

            Input:
                show_b: Wheather user want to create a window for plot.
            Output:
                total_dict: {comp_data_name: {"method_name": res_value}}
        """

        total_dict = self.total_correlation()
        roll_dict  = self.rolling_correlation(self.mov_win_size, show_b, save_p)


        return total_dict

    def rolling_correlation(self, win_size = 10, plot_b=False, save_p="../100_DB"):
        """
            This function is used to calculate the rolling correlation of data with
            specific window size also is able to plot the result.

            Input:
                win_size: Rolling window size
                plot_b: Wheather to plot the result.
            Return:
                Res_dict: {comp_data_name: {"method_name": res_value}}
        """
        Res_dict = {}
        half_win = int(math.ceil(win_size/2))

        tar_data  = self.data_dict["tar_data"]
        data_size = tar_data.shape

        draw_x_list = []
        draw_y_list = []
        draw_type_list = []
        legend_list = []

        for m_nu in range(0, len(self.info_dict["method_list"])):

            if self.info_dict["method_list"][m_nu] == "Pearsons":
                cal_func = self.cal_pearson
            elif self.info_dict["method_list"][m_nu] == "Spearmanr":
                cal_func = self.cal_spearmanr
            else:
                raise(ValueError("User set unkonw corr"))

            for d_nu in range(0, len(self.data_dict["comp_data_list"])):
                this_corrlation_list = []

                this_comp_data = self.data_dict["comp_data_list"][d_nu]

                for i in range(win_size, data_size[0]-win_size):
                    this_corrlation_list.append(cal_func(
                        tar_data[i-win_size:i+win_size],    
                        this_comp_data[i-win_size:i+win_size]
                    ))
                
                this_name = "{}_{}_{}".format(self.info_dict["data_name_list"][0],
                        self.info_dict["data_name_list"][d_nu + 1], self.info_dict["method_list"][m_nu])

                draw_x_list.append(list(np.arange(win_size, data_size[0]-win_size)))
                draw_y_list.append(this_corrlation_list)
                draw_type_list.append("-")
                legend_list.append(this_name)

                Res_dict[this_name] = np.array(this_corrlation_list)
                
        if plot_b:
            plotter = JP_P.JP_plotter()

            save_dict = {
                "save_b": True, "save_p": save_p, "save_n": "rooling_corr"
            }

            info_dict = {"title": self.info_dict["data_set_name"], "x_label": "Index", "y_label": "correlation"}
            plotter.plot_2d(draw_x_list, draw_y_list, info_dict, hold_bool=False,
                type_list=draw_type_list, legend_list=legend_list, save_dict=save_dict)

        return Res_dict

    def total_correlation(self):
        """
            This function is used to calculate the correlation of whole data between
            tar data and compdata.

            Input:
                None
            Output:
                Res_dict: {comp_data_name: {"method_name": res_value}}
        """

        Res_dict = {}

        for m_nu in range(0, len(self.info_dict["method_list"])):
            if self.info_dict["method_list"][m_nu] == "Pearsons":
                cal_func = self.cal_pearson
            elif self.info_dict["method_list"][m_nu] == "Spearmanr":
                cal_func = self.cal_spearmanr
            else:
                raise(ValueError("User set unkonw corr"))
            
            for d_nu in range(0, len(self.data_dict["comp_data_list"])):
                this_score = cal_func(self.data_dict["tar_data"], 
                    self.data_dict["comp_data_list"][d_nu])

                this_name = "{}_{}_{}".format(self.info_dict["data_name_list"][0],
                        self.info_dict["data_name_list"][d_nu + 1], self.info_dict["method_list"][m_nu])
                Res_dict[this_name] = this_score

        return Res_dict

    def cal_spearmanr(self, data_tar, data_comp):
        """
            This function is used to calculate the spearman correlation of the data
            Input:
                data_tar: data_1
                data_comp: data_2
            Return:
                correlation: Calculate result
        """

        score = stats.spearmanr(data_tar, data_comp)
        correlation = score[0]

        # print("DB:> IN correlation_comp.py L156:> score: {}".format(score))
        # print("DB:> L157:> tar: mean {} std {}".format(np.mean(data_tar), np.std(data_tar)))
        # print("DB:> L157:> comp: mean {} std {}".format(np.mean(data_comp), np.std(data_comp)))
        # print("DB:> L157:> comp data {}".format(data_comp))

        return correlation

    def cal_pearson(self, data_tar, data_comp):
        """
            This function is used to calculate the pearson correlation of the data
            Input:
                data_tar: data_1
                data_comp: data_2
            Output:
                correlation: Calculate result
        """

        score = stats.pearsonr(data_tar, data_comp)

        correlation = score[0]

        return correlation


def test():
    a = np.random.rand(1,10)
    noise = np.random.rand(1,10)

    b = 100*a + noise
    res = noise
    res_2 = 5+b

    data_dict = {"tar_data": b[0, :], "comp_data_list": [res[0,:], res_2[0,:]]}
    info_dict = {"method_list": ["Pearsons", "Spearmanr"],
        "data_name_list": ["src", "res", "res2"]}

    comper = Correlation_comp(data_dict=data_dict, info_dict=info_dict)
    res = comper.exe()
    print("res: \n{}".format(res))

if __name__ == "__main__":
    test()


