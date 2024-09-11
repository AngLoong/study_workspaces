"""
定义读板类型
"""

import numpy as np
import pandas as pd
# from mrs_serial import SerialCommunication
from mrs_communication import EquipmentCommunication
import mrs_analysis


class ReadPlate(object):
    """
    读板类，进行酶标读板相关的操作
    """

    def __init__(self):
        header = []
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        for j in num:
            for i in letter:
                header.append(i+j)
        print(header)
        self.data = pd.Series(0.0, header)
        print(self.data)
        self.filter = {"du": 1, "first filter num": 2, "second filter num": 4}
        print(self.filter)
        self.shake = {"strength": 2, "seconds": 0}
        print(self.shake)
        # self.mode = 1
        self.kinetics = {"times": 1, "minutes": 0, "seconds": 5}
        print(self.kinetics)
        # self.com = SerialCommunication()
        self.com = EquipmentCommunication()

    def door(self):
        """
        self.com.connect()
        self.com.send_door()
        self.com.disconnect()
        """
        self.com.open_or_close_door()

    def read_plate(self):
        """
        self.com.connect()
        self.com.send_read_plate(self.filter["du"],
                                 self.filter["first_filter_num"],
                                 self.filter["second_filter_num"],
                                 self.shake["strength"],
                                 self.shake["seconds"],
                                 1,
                                 self.kinetics["times"],
                                 self.kinetics["seconds"],
                                 self.kinetics["minutes"])
        result = self.com.receive_result()
        self.com.disconnect()
        """
        result = self.com.read_plate(self.filter["du"],
                                     self.filter["first filter num"],
                                     self.filter["second filter num"],
                                     self.shake["strength"],
                                     self.shake["seconds"])
        for i in range(96):
            self.data[i] = result[i]
        print(self.data)
        return result

    def read_kinetics(self):
        """
        tmp_df = pd.DataFrame()
        self.com.connect()
        self.com.send_read_plate(self.filter["du"],\
                            self.filter["first_filter_num"],\
                            self.filter["second_filter_num"],\
                            self.shake["strength"],\
                            self.shake["seconds"],\
                            3,\
                            self.kinetics["times"],\
                            self.kinetics["seconds"],\
                            self.kinetics["minutes"])
        for i in range(self.kinetics["times"]):
            result = self.com.receive_result()
            for j in range(96):
                self.data[j] = result[j]
            tmp_df.insert(i, str(i+1), self.data)
            print(result)
        self.com.disconnect()
        print(tmp_df)
        return tmp_df
        """
        pass


if __name__ == '__main__':
    aa = ReadPlate()
    while True:
        cc = input("input command:")
        if cc == "o":
            aa.door()
        elif cc == "m":
            rr = aa.read_plate()
            print("============\n")
            print(rr)
        else:
            exit()


