"""
定义通讯协议
"""

import numpy as np
import pandas as pd
from mrs_serial import SerialCommunication


class EquipmentCommunication(object):
    """定义设备通讯的协议

    定义软件和设备的通讯协议接口。

    Attributes:
        door_status:仓门状态，1：开，0：关
    """

    def __init__(self):
        self.door_status = 0
        self.com = SerialCommunication()

    def open_or_close_door(self):
        self.com.connect()
        self.com.send_door()
        self.com.disconnect()

    def open_door(self):
        pass

    def close_door(self):
        pass

    def read_plate(self, dua, first_filter_num, second_filter_num,
                   shake_strength, shake_seconds):
        self.com.connect()
        self.com.send_read_plate(dua, first_filter_num, second_filter_num,
                                 shake_strength, shake_seconds,
                                 1, 3, 1, 0)
        result = self.com.receive_result()
        self.com.disconnect()
        return result

    def read_kinetics(self):
        pass
