"""
功能模块
"""

import numpy as np
import pandas as pd
import time
from mrs_read_plate import ReadPlate
from mrs_analysis import ana_stability
from mrs_file import exort_plate_od_to_csv


def measure_test():
    id = input("输入仪器编号")
    if input("确认仪器编号: " + str(id) + "\n并输入y") == 'y':
        read_plate = ReadPlate()
        read_plate.mode = 1
        read_plate.shake["strength"] = 2
        read_plate.shake["seconds"] = 60
        read_plate.filter["du"] = 1
        read_plate.filter["first_filter_num"] = 1
        read_plate.filter["second_filter_num"] = 4
        read_plate.door()
        file_name = "./record/"+id+".csv"
        if input("放入待测酶标板，并按y") == 'y':
            measure_time = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
            print(measure_time)
            read_plate.read_plate()
            print(read_plate.data)
            ser_time = pd.Series({"measure time:":measure_time,"":""})
            ser_time.to_csv(file_name,header=False)
            ser_temp = pd.Series({"filter num :":read_plate.filter["first_filter_num"]})
            ser_temp.to_csv(file_name,header=False,mode="a+")
            exort_plate_od_to_csv(file_name,read_plate.data.tolist(),"a+")
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    measure_test()