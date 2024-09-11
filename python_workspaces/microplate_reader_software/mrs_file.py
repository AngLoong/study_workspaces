"""
文件操作,涉及文件的存储与读入，主要对文件的内容进行格式化。
"""

import pandas as pd
import numpy as np
import os


def export_plate_od_to_csv(file_name, od_data, write_mode):
    """以96孔板的形式导出为csv文件

    :param file_name:文件路径
    :param od_data: OD数据，列表
    :param write_mode: ”a+"表示在文末写入，“w“表示从新写入
    :return:
    """
    list_col = []
    for kI in range(12):
        list_col.append(od_data[kI * 8:kI * 8 + 8])
    col = list(map(chr, range(ord('A'), ord('H') + 1)))
    ind = [str(x) for x in range(1, 13)]
    export_data1 = pd.DataFrame(list_col, index=ind, columns=col)
    export_data1 = export_data1.transpose()  # 翻转矩阵
    export_data1.to_csv(file_name, mode=write_mode)


def export_plate_to_csv(du, first, second, od):  # TODO(ayl):可能删除
    export_info = pd.Series({"du:": "1", "first filter:": "450", "second filter:": "630", " ": " "})
    print(export_info)
    list_col = []
    for i in range(12):
        list_col.append(od[i * 8:i * 8 + 8])
    print(list_col)
    col = list(map(chr, range(ord('A'), ord('H') + 1)))
    ind = [str(x) for x in range(1, 13)]
    print("IND:", ind)
    print("COL:", col)
    export_data1 = pd.DataFrame(list_col, index=ind, columns=col)
    export_data1 = export_data1.transpose()
    export_data = pd.DataFrame([{"1": 1.2, "2": 2.3, "3": 1.1, "4": 2.1, "5": 1.6, "6": 3.1,
                                 "7": 1.8, "8": 0.2, "9": 1.1, "10": 3.0, "11": 2.1, "12": 0.7},
                                {"1": 1.1, "2": 2.0, "3": 1.0, "4": 2.0, "5": 1.0, "6": 3.0,
                                 "7": 1.0, "8": 0.2, "9": 1.0, "10": 3.0, "11": 2.0, "12": 0.7}],
                               index=["A", "B"])
    print(export_data)
    export_info.to_csv("./22.csv", header=False, )
    export_data.to_csv("./22.csv", mode="a+")
    export_data1.to_csv("./22.csv", mode="a+")


def get_root_path():
    """取得根目录路径

    :return: 路径字符串
    """
    return os.getcwd()


def check_dir_exist(path_str):
    """检查目录路径是否存在

    :param path_str: 路径字符串
    :return: 1，存在；0，不存在
    """
    return os.path.isdir(path_str)


def link_dir(path1, path2):
    """连接目录路径

    将两段路径字符串连接起来，避免系统路径分隔符不同造成的差异。

    :param path1: 前段路径
    :param path2: 后段路径
    :return: 连接后的路径
    """
    return os.path.join(path1, path2)


def new_folder(position_path, folder_name):
    """在指定路径下建立目录文件夹

    :param position_path:指定的路径
    :param folder_name: 文件夹的名字
    :return: 0，创建成功；1，创建失败
    """
    if not os.path.isdir(position_path):
        print("no path")
        return -1
    else:
        os.mkdir(os.path.join(position_path, folder_name))
        return 0


if __name__ == '__main__':
    li_od = [0.5 for x in range(96)]
    export_plate_od_to_csv("2011.csv", li_od, "w")
