"""
文件操作
"""

import pandas as pd
import numpy as np
from mrs_read_plate import ReadPlate


def export_plate_to_csv(du, first, second, od):
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
    export_data = pd.DataFrame([{"1": 1.2, "2": 2.3, "3": 1.1, "4": 2.1, "5": 1.6, "6": 3.1, \
                                 "7": 1.8, "8": 0.2, "9": 1.1, "10": 3.0, "11": 2.1, "12": 0.7}, \
                                {"1": 1.1, "2": 2.0, "3": 1.0, "4": 2.0, "5": 1.0, "6": 3.0, \
                                 "7": 1.0, "8": 0.2, "9": 1.0, "10": 3.0, "11": 2.0, "12": 0.7}], \
                               index=["A", "B"])
    print(export_data)
    export_info.to_csv("./22.csv", header=False, )
    export_data.to_csv("./22.csv", mode="a+")
    export_data1.to_csv("./22.csv", mode="a+")


if __name__ == '__main__':
    data = []
    for i in range(12):
        for j in range(8):
            data.append(i * 10 + j)
    export_plate_to_csv(1, 1, 1, data)
