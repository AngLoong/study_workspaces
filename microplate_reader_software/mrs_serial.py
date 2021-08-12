"""
串口通讯
"""
import pandas as pd
import serial
import serial.tools.list_ports
from mrs_config import ConfigProperty

class SerialCommunication():
    """

    """

    command_send_head = bytes(b'\x7f\xf7\xaa')
    command_send_tail = bytes(b'\xbb\xfe\xff')
    command_send_door = bytes(b'\xe1\xe2\xe3\xee\xee\xee\xee\xee\xee\xee')
    command_receive_head = bytes(b'\x7c\xc7\x7d\xd7')
    command_receive_tail = bytes(b'\xfc\xfd\xfe\xff')

    def __init__(self,default_baud = 115200,default_port = "COM6",default_time_out = None):
        cf = ConfigProperty()
        cf.load()
        self.port = cf.attributes["serial settings"]["com"]
        self.baud_rate = cf.attributes["serial settings"]["baud"]
        self.time_out = cf.attributes["serial settings"]["time out"]
        #self.__ser__ = None

    def connect(self):
        self.__ser__ = serial.Serial(self.port,self.baud_rate,timeout=self.time_out)
        print("connect ok!!")

    def disconnect(self):
        self.__ser__.close()
        print("disconnect ok!!")

    def send_door(self):
        ret = self.__ser__.write(self.command_send_head+self.command_send_door+self.command_send_tail)
        return ret

    def __change_command_to_float(self,data):
        num = int(data[0])
        num += int(data[2]) * 0.1
        num += int(data[3]) * 0.01
        num += int(data[4]) * 0.001
        return num

    def send_read_plate(self,dua,first_filter_num,second_filter_num,\
                   shake_strength,shake_seconds,\
                   mode,\
                   kinetics_times,kinetics_seconds,kinetics_minutes):
        command4 = bytes(b'\x01')
        command5 = bytes([dua,first_filter_num,second_filter_num,\
                         shake_strength,shake_seconds,
                         mode,\
                         kinetics_times,kinetics_seconds,kinetics_minutes])
        command_total = self.command_send_head+command4+command5+self.command_send_tail
        ret = self.__ser__.write(command_total)
        return ret

    def receive_result(self):
        re_data = self.__ser__.read(488)
        if re_data[:4] == self.command_receive_head and \
            re_data[-4:] == self.command_receive_tail:
            num = 4
            list_data = []
            for i in range(96):
                list_data.append(self.__change_command_to_float(re_data[num:num + 5]))
                num += 5
            return list_data
        else:
            print(re_data[:4])
            print(re_data[-4:])
            return []


if __name__ == '__main__':
    """
    ss = SerialCommunication();
    ss.connect()
    tem = ss.read_plate(1,2,4,2,0,1,1,0,0)
    print(tem)
    ss.disconnect()
    """
    """
    command_send_4 = bytes(b'\x01')  #读板测量
    command_send_5 = bytes(b'\x01')  #单波长
    command_send_6 = bytes(b'\x02')  #主波长
    command_send_7 = bytes(b'\x04')  #副波长
    command_send_8 = bytes(b'\x02')  #振板强度
    command_send_9 = bytes(b'\x00')  #振板时间，单位s
    command_send_10 = bytes(b'\x01')  #测量方法：1，终点；2，两点；3，动力学
    command_send_11 = bytes(b'\x01')  #动力学次数
    command_send_12 = bytes(b'\x00')  #动力学间隔时间s
    command_send_13 = bytes(b'\x00')  #动力学间隔时间m

    command_send = command_send_4+command_send_5+command_send_6+command_send_7+command_send_8+command_send_9+command_send_10+command_send_11+command_send_12+command_send_13

    portx = "COM6"
    bps = 9600
    timex = None #None表示永远等待，单位为秒
    ser = serial.Serial(portx,bps,timeout=timex)
    print("串口参数详情：",ser)

    command_receive_head = bytes(b'\x7f\xf7\x7d\xd7')
    command_receive_tail = bytes(b'\xfc\xfd\xfe\xff')

    result = ser.write(command_send)

    print("写字数",result)

    re_data = ser.read(488)
    print(re_data[:4])
    print(re_data[-4:])
    num = 4
    list_data = []
    for i in range(96):
        list_data.append(re_data[num:num+5])
        num += 5

    print(list_data[0].hex())
    print(change_to_num(list_data[0]))
    print(change_to_num(list_data[1]))
    print(len(list_data))
    print(list_data[0])
    print(type(re_data))
    print(re_data.hex())

    print("-------------")
    ser.close()
    """
