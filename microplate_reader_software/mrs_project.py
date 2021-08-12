"""
定义项目类，对项目进行管理，每个会话调用项目进行管理
"""


import numpy as np
import pandas as pd
from mrs_read_plate import ReadPlate


class MeasureLayout(object):
    """
    测量布局类
    """

    layout_types = ['none','smp','std','blk','nc','pc']

    def __init__(self):
        header = []
        letter = list(map(chr, range(ord('A'), ord('H') + 1)))
        num = [str(x) for x in range(1, 13)]
        for j in num:
            for i in letter:
                header.append(i + j)
        self.type = pd.Series(0, index=header)
        self.num = pd.Series(0, index=header)
        #print(self.type)
        #print(self.num)

    def __str__(self):
        ret = ''
        for i in range(96):
            ret += self.type.index[i] + ':' +\
                   MeasureLayout.layout_types[self.type.values[i]] +\
                   str(self.num.values[i]) +'\n'
        return ret


class MeasureProcess(object):
    """
    檢測流程類
    """

    process_types = ['none', 'measure', 'kinetic', 'door', 'pause']

    def __init__(self):
        self._id = 0
        self._type = 0
        self._para = None

    def __str__(self):
        ret = 'ID:'
        ret += str(self._id)+'\n'
        ret += "TYPE:"+MeasureProcess.process_types[self._type]+\
            '\n'
        ret += "PARA:"+str(self._para)
        return ret

    def clear_process(self):
        self._id = 0
        self._type = 0
        self._para = None

    def set_process_pause(self,id,minutes=0,seconds=5):
        self._id = id
        self._type = 4
        self._para={"minutes":0,"seconds":0}
        self._para["minutes"] = minutes
        self._para["seconds"] = seconds

    def set_process_door(self,id):
        self._id = id
        self._type = 3
        self._para = None

    def set_process_measure(self,id,\
                            du=1,first_filter_num=2,second_filter_num=4,\
                            shake_strength=2,shake_seconds=0):
        self._id = id
        self._type = 1
        filter_para = {"du":du,"first_filter_num":first_filter_num,"second_filter_num":second_filter_num}
        shake_para = {"strength":shake_strength,"seconds":shake_seconds}
        self._para={"filter":filter_para,"shake":shake_para}

    def set_process_kinetics(self,id,\
                             du=1,first_filter_num=2,second_filter_num=4,\
                             shake_strength=2,shake_seconds=0,\
                             kinetics_times=5,kinetics_minutes=0,kinetics_seconds=5):
        self._id = id
        self._type = 2
        filter_para = {"du": du, "first_filter_num": first_filter_num, "second_filter_num": second_filter_num}
        shake_para = {"strength": shake_strength, "seconds": shake_seconds}
        kinetics_para = {"times":kinetics_times,"minutes":kinetics_minutes,"seconds":kinetics_seconds}
        self._para = {"filter": filter_para, "shake": shake_para,"kinetics":kinetics_para}

    def execute_process(self):
        if self._type == 0:
            pass
        elif self._type == 1:
            read_plate = ReadPlate()
            for key in read_plate.filter.keys():
                read_plate.filter[key] = self._para["filter"][key]
            for key in read_plate.shake.keys():
                read_plate.shake[key] = self._para["shake"][key]
            data=read_plate.read_plate()
            print(data)
        elif self._type ==2:
            read_plate = ReadPlate()
            for key in read_plate.filter.keys():
                read_plate.filter[key] = self._para["filter"][key]
            for key in read_plate.shake.keys():
                read_plate.shake[key] = self._para["shake"][key]
            for key in read_plate.kinetics.keys():
                read_plate.kinetics[key] = self._para["kinetics"][key]
            data = read_plate.read_kinetics()

class MeasureProject(object):
    """
    测量项目类，对测量项目进行管理
    """

    calculate_types = ['blank subtraction', 'average', 'SD', 'CV%', \
                       'standard curve', 'kinetic', \
                       'quantitative', 'qualitative']

    def __init__(self):
        self.id = 1
        self.name = 'test1'
        self.note = 'New project'
        self.layout = MeasureLayout()
        self.process = []
        self.results = []
        self.report = []


if __name__ == '__main__':
    layout = MeasureLayout()
    print(layout)
    process = MeasureProcess()
    if process._para == None:
        print('yyy')
    else:
        print('NNN')
    print(process)
    process.set_process_pause(1)
    print(process)
    process.set_process_measure(2)
    print(process)
    process.execute_process()
    """
    read_plate = ReadPlate()
    read_plate.filter["du"] = 1
    read_plate.filter["first_filter_num"] = 2
    read_plate.filter["second_filter_num"] = 4
    read_plate.shake["strength"] = 2
    read_plate.shake["seconds"] = 5
    read_plate.mode = 3
    read_plate.kinetics["times"] = 1
    read_plate.kinetics["minutes"] = 0
    read_plate.kinetics["seconds"] = 3
    df_result = read_plate.read_kinetics()
    print(df_result)
    """