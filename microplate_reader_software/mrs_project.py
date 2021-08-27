"""
定义项目类，对项目进行管理，每个会话调用项目进行管理
"""


import numpy as np
import pandas as pd
import time
import json
from mrs_read_plate import ReadPlate


class MeasureLayout(object):
    """
    测量布局类
    """

    layout_types = ['none', 'smp', 'std', 'blk', 'nc', 'pc']

    def __init__(self):
        self.id = 0
        self.name = 'new layout'
        header = []
        letter = list(map(chr, range(ord('A'), ord('H') + 1)))
        num = [str(x) for x in range(1, 13)]
        for j in num:
            for i in letter:
                header.append(i + j)
        self.type = pd.Series(0, index=header)
        self.num = pd.Series(0, index=header)
        """
        print(self.type)
        print(self.num)
        """

    def __str__(self):
        ret = "LAYOUT ID:" + str(self.id) + "\n"
        ret += "NAME:" + self.name + "\n"
        for i in range(96):
            ret += self.type.index[i] + ':' +\
                   MeasureLayout.layout_types[self.type.values[i]] +\
                   str(self.num.values[i]) + '\n'
        return ret

    def to_dict(self):
        ret_dict = {"id": self.id,
                    "name": self.name,
                    "type list": self.type.tolist(),
                    "num list": self.num.tolist()}
        return ret_dict

    def from_dict(self, temp_dict):
        self.id = temp_dict["id"]
        self.name = temp_dict["name"]
        for i in range(96):
            self.type[i] = temp_dict["type list"][i]
        for i in range(96):
            self.num[i] = temp_dict["num list"][i]


class MeasureProcess(object):
    """
    检测流程类 
    """

    process_types = ['none', 'measure', 'kinetic', 'door', 'pause']

    def __init__(self):
        self._id = 0
        self._type = 0
        self._para = None

    def __str__(self):
        ret = 'ID:'
        ret += str(self._id)+'\n'
        ret += "TYPE:"+MeasureProcess.process_types[self._type] +\
            '\n'
        ret += "PARA:"+str(self._para)
        return ret

    def clear_process(self):
        self._id = 0
        self._type = 0
        self._para = None

    def set_process_pause(self, id_num, minutes=0, seconds=5):
        self._id = id_num
        self._type = 4
        self._para = {"minutes": minutes, "seconds": seconds}

    def set_process_door(self, id_num):
        self._id = id_num
        self._type = 3
        self._para = None

    def set_process_measure(self, id_num,
                            du=1, first_filter_num=2, second_filter_num=4,
                            shake_strength=2, shake_seconds=0):
        self._id = id_num
        self._type = 1
        filter_para = {"du": du, "first_filter_num": first_filter_num, "second_filter_num": second_filter_num}
        shake_para = {"strength": shake_strength, "seconds": shake_seconds}
        self._para = {"filter": filter_para, "shake": shake_para}

    def set_process_kinetics(self, id_num,
                             du=1, first_filter_num=2, second_filter_num=4,
                             shake_strength=2, shake_seconds=0,
                             kinetics_times=5, kinetics_minutes=0, kinetics_seconds=5):
        self._id = id_num
        self._type = 2
        filter_para = {"du": du, "first_filter_num": first_filter_num, "second_filter_num": second_filter_num}
        shake_para = {"strength": shake_strength, "seconds": shake_seconds}
        kinetics_para = {"times": kinetics_times, "minutes": kinetics_minutes, "seconds": kinetics_seconds}
        self._para = {"filter": filter_para, "shake": shake_para, "kinetics": kinetics_para}

    def execute_process(self):
        if self._type == 0:
            pass
        elif self._type == 1:
            read_plate = ReadPlate()
            for key in read_plate.filter.keys():
                read_plate.filter[key] = self._para["filter"][key]
            for key in read_plate.shake.keys():
                read_plate.shake[key] = self._para["shake"][key]
            read_plate.read_plate()
            data = read_plate.data
            print("=============\n")
            print(data)
        elif self._type == 2:
            data_list = []
            read_plate = ReadPlate()
            for key in read_plate.filter.keys():
                read_plate.filter[key] = self._para["filter"][key]
            for key in read_plate.shake.keys():
                read_plate.shake[key] = self._para["shake"][key]
            for key in read_plate.kinetics.keys():
                read_plate.kinetics[key] = self._para["kinetics"][key]
            for i in range(self._para["kinetics"]["times"]):
                read_plate.read_plate()
                data_list.append(read_plate.data)
                if i < self._para["kinetics"]["times"] - 1:
                    time.sleep(self._para["kinetics"]["minutes"]*60 + self._para["kinetics"]["seconds"])
            print("-----------------")
            print(data_list)


class MeasureCalculate(object):
    """
    计算方法类
    """
    calculate_types = ['none', 'blank subtraction', 'average', 'SD', 'CV%',
                       'standard curve', 'kinetic',
                       'quantitative', 'qualitative']
    quantitative_concentration_handle = ['concentration', 'log']
    quantitative_od_handle = ['od', 'log', 'bi/b0*100%']
    curve_types = ['linear']

    def __init__(self):
        self._id = 0
        self._type = 0
        self._para = None

    def __str__(self):
        ret = 'ID:'
        ret += str(self._id)+'\n'
        ret += "TYPE:"+MeasureCalculate.calculate_types[self._type] +\
            '\n'
        ret += "PARA:"+str(self._para)
        return ret

    def clear_calculate(self):
        self._id = 0
        self._type = 0
        self._para = None

    def set_calculate_blank_subtraction(self, id_num):
        self._id = id_num
        self._type = 1
        self._para = None

    def set_calculate_average(self, id_num, objective_area):
        self._id = id_num
        self._type = 2
        self._para = {"objective area": objective_area}

    def set_calculate_sd(self, id_num, objective_area):
        self._id = id_num
        self._type = 3
        self._para = {"objective area": objective_area}

    def set_calculate_cv(self, id_num, objective_area):
        self._id = id_num
        self._type = 4
        self._para = {"objective area": objective_area}

    def set_calculate_standard_curve(self, id_num):
        self._id = id_num
        self._type = 5
        self._para = None

    def set_calculate_kinetic_curve(self, id_num, objective_area):
        self._id = id_num
        self._type = 6
        self._para = {"objective area": objective_area}

    def set_calculate_quantitative(self, id_num, curve_type=0, concentration_handle=0, od_handle=0):
        self._id = id_num
        self._type = 7
        self._para = {"curve type": curve_type, "concentration handle": concentration_handle, "od handle": od_handle}

    def set_calculate_qualitative(self, id_num, cutoff_formula):
        self._id = id_num
        self._type = 8
        self._para = {"cutoff_formula": cutoff_formula}

    # TODO:计算操作


class MeasureResult(object):
    """
    测量结果类
    """

    def __init__(self):
        self._count = 0
        self._current = 0
        self.time = None
        header = []
        letter = list(map(chr, range(ord('A'), ord('H') + 1)))
        num = [str(x) for x in range(1, 13)]
        for j in num:
            for i in letter:
                header.append(i + j)
        self.data_current_plate = pd.Series(0.0, index=header)
        self.data_df = pd.DataFrame(index=header)

    def __str__(self):
        ret = "count:" + str(self._count) + "\n"
        ret += "time:" + str(self.time) + "\n"
        ret += "data:" + str(self.data_df) + "\n"
        ret += "current plate data:\n" + str(self._current) + "\n" + str(self.data_current_plate)
        return ret

    def __clear_current_data(self):
        for i in range(96):
            self.data_current_plate[i] = 0

    def get_plate_od_from_list(self, od_list):
        for i in range(96):
            self.data_current_plate[i] = od_list[i]
        self.data_df.insert(self.data_df.shape[1], str(self.data_df.shape[1]+1), od_list)
        self._count += 1
        self._current = self.data_df.shape[1]

    def select_current_plate(self, num):
        if num < self._count + 1:
            self._current = num
            self.data_current_plate = self.data_df.loc[:,str(self._current)]
            return True
        else:
            self.__clear_current_data()
            return False


class MeasureProject(object):
    """
    测量项目类，对测量项目进行管理
    """

    file_path = "./projects/"

    def __init__(self):
        self.id = 0
        self.name = 'new project'
        self.note = 'New project'
        self.layout = MeasureLayout()
        self.process_list = []
        self.calculate_list = []
        self.results = MeasureResult()
        self.reports = None

    def __str__(self):
        ret = "ID:" + str(self.id) + "\n"
        ret += "NAME:" + self.name + "\n"
        ret += "NOTE:" + self.note + "\n"
        ret += "LAYOUT" + str(self.layout) + "\n"
        ret += "PROCESS:" + str(self.process_list) + "\n"
        ret += "CALCULATE:" + str(self.calculate_list) + "\n"
        ret += "RESULT:" + str(self.results) + "\n"
        return ret

    def clear(self):
        self.id = 0
        self.name = 'new project'
        self.note = 'New project'
        self.layout = MeasureLayout()
        self.process_list = []
        self.calculate_list = []
        self.results = MeasureResult()
        self.reports = None

    def save(self):
        temp_path = MeasureProject.file_path + str(self.id) + ".json"
        temp_st = {"id": self.id,
                   "name": self.name,
                   "note": self.note,
                   "layout": self.layout.to_dict(),
                   "process list": self.process_list,
                   "calculate list": self.calculate_list}
        with open(temp_path, "w", encoding='utf-8') as f:
            json.dump(temp_st, f, indent=2)

    def load(self, id_num):
        temp_path = MeasureProject.file_path + str(id_num) + ".json"
        with open(temp_path, "r", encoding='utf-8') as f:
             temp_st = json.load(f)
        self.id = temp_st["id"]
        self.name = temp_st["name"]
        self.note = temp_st["note"]
        self.layout.from_dict(temp_st["layout"])
        self.process_list = temp_st["process list"]
        self.calculate_list = temp_st["calculate list"]


if __name__ == '__main__':
    pass