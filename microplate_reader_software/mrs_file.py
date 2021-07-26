"""
文件操作
"""


import pandas as pd
import numpy as np
from mrs_read_plate import ReadPlate


def export_to_csv():
    export_info = pd.Series({"du:":"1","first filter:":"450","second filter:":"630"," ":" "})
    print(export_info)
    export_data = pd.DataFrame([{"1":1.2,"2":2.3,"3":1.1,"4":2.1,"5":1.6,"6":3.1,\
                                "7":1.8,"8":0.2,"9":1.1,"10":3.0,"11":2.1,"12":0.7},\
                                {"1":1.1,"2":2.0,"3":1.0,"4":2.0,"5":1.0,"6":3.0,\
                                "7":1.0,"8":0.2,"9":1.0,"10":3.0,"11":2.0,"12":0.7}],\
                               index=["A","B"])
    print(export_data)
    export_info.to_csv("./22.csv",header=False,)
    export_data.to_csv("./22.csv",mode="a+")


if __name__ == '__main__':
    export_to_csv()