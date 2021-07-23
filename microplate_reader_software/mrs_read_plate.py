"""
定义读板类型
"""

import numpy as np
import pandas as pd
from mrs_serial import SerialCommunication


class ReadPlate():
    """
    读板类，进行酶标读板相关的操作
    """

    def __init__(self):
        header = []
        letter = ['A','B','C','D','E','F','G','H']
        num = ['1','2','3','4','5','6','7','8','9','10','11','12']
        for j in num:
            for i in letter:
                header.append(i+j)
        print(header)
        self.data=pd.Series(0.0,header)
        print(self.data)
        self.filter = {"du":1,"first_filter_num":2,"second_filter_num":4}
        print(self.filter)
        self.shake = {"strength":2,"seconds":0}
        print(self.shake)
        self.mode = 1
        self.kinetics = {"times":1,"minutes":0,"seconds":5}
        print(self.kinetics)
        self.com = SerialCommunication()

    def door(self):
        self.com.connect()
        self.com.door()
        self.com.disconnect()

    def read_plate(self):
        self.com.connect()
        result = self.com.read_plate(self.filter["du"],\
                            self.filter["first_filter_num"],\
                            self.filter["second_filter_num"],\
                            self.shake["strength"],\
                            self.shake["seconds"],\
                            self.mode,\
                            self.kinetics["times"],\
                            self.kinetics["seconds"],\
                            self.kinetics["minutes"])
        self.com.disconnect()
        for i in range(96):
            self.data[i] = result[i]
        print(self.data)
        print("A1:",self.data["A1"])
        print("B1:",self.data["B1"])
        print("A2:",self.data["A2"])

if __name__ == '__main__':
    aa = ReadPlate()
    aa.read_plate()