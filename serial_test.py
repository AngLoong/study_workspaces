#!python3
#v0.1.0

""""
    学习python 串口通讯的程序
"""

import serial
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())
print(port_list)

if len(port_list) == 0:
    print("no ports")
else:
    for i in range(0,len(port_list)):
        print(port_list[i])

try:
    portx = "COM6"
    bps = 115200
    timex = None #None表示永远等待，单位为秒
    ser = serial.Serial(portx,bps,timeout=timex)
    print("串口参数详情：",ser)

    result = ser.write(bytes(b'\xee\xb1\x00\x00\x06\xff\xfc\xff\xff'))

    print("写字数",result)

    for count in range(5):
        print(ser.read().hex())

    print("-------------")
    ser.close()

except Exception as e:
    print("error:",e)

