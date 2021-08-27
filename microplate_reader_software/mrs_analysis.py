"""
分析仪器性能参数
"""


import numpy as np
import pandas as pd


def ana_stability(data):  # TODO:改名
    df = pd.DataFrame()
    df = data
    li_err = []
    li_max = []
    li_min = []
    li_check = []
    for i in range(df.shape[0]):
        row = df.iloc[i]
        row_max = max(row)
        row_min = min(row)
        li_max.append(row_max)
        li_min.append(row_min)
        li_err.append(row_max-row_min)
        # print("loop",i,row_max,"->",row_min)
        # max.append(row_max)
        # min.append(row_min)
    print("li-max:", li_max)
    print("li-min:", li_min)
    print("li-err:", li_err)
    for i in range(len(li_err)):
        if li_min[i] < 2:
            che = True if li_err[i] < 0.01 else False
        if 2 < li_min[i] < 3:
            che = True if li_err[i] < 0.1 else False
        else:
            che = True
        li_check.append(che)
    print("check:", li_check)
    df.insert(df.shape[1], 'max', li_max)
    df.insert(df.shape[1], 'min', li_min)
    df.insert(df.shape[1], 'err', li_err)
    df.insert(df.shape[1], 'check', li_check)
    df.to_csv("./cache/stability.csv")
    print(df)
    return df


def ana_blank_subtraction(target, blank):
    """
    OD减去空白
    :param target:目标值
    :param blank: 空白值
    :return:od value without blank
    """
    temp_ret = target - blank
    if ret < 0:
        return 0
    else:
        return temp_ret


def ana_get_average(target_list):
    """
    求平均值
    :param target_list:
    :return:
    """
    temp_arr = np.array(target_list)
    return temp_arr.mean()


def ana_get_sd(target_list):
    """
    计算标准差
    :param target_list:
    :return:
    """
    temp_arr = np.array(target_list)
    return temp_arr.std()


def ana_get_cv(target_list):
    """
    计算变异系数CV
    :param target_list:数据源列表
    :return: 变异系数
    """
    temp_arr = np.array(target_list)
    return temp_arr.std()/temp_arr.mean()


def calculate_custom_formula(exp,li_var,li_value):
    if len(li_var) != len(li_value):
        return None
    else:
        for i in range(len(li_var)):
            temp = li_var[i] + "=" + str(li_value[i])
            exec(temp)
        return eval(exp)


if __name__ == '__main__':
    li1 = ['a','b','c']
    li2 = [1,2,3]
    exp = "a*b+c**2"
    rr = calculate_custom_formula(exp,li1,li2)
    print(rr)
