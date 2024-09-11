"""
定义项目类，对项目进行管理，每个会话调用项目进行管理
"""

import numpy as np
import pandas as pd
import time
import json
from mrs_read_plate import ReadPlate
import mrs_file


class MeasureLayout(object):
    """测量布局类
    
    用于保存、设置测量项目的布局

    Attributes:
        id:ID号,保存布局时需要
        name:布局名称，保存布局时需要
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
            ret += self.type.index[i] + ':' + \
                   MeasureLayout.layout_types[self.type.values[i]] + \
                   str(self.num.values[i]) + '\n'
        return ret

    def to_dict(self):
        """转换为字典

        将参数转换为字典形式返回

        :return:参数，字典类型
        """
        ret_dict = {"id": self.id,
                    "name": self.name,
                    "type list": self.type.tolist(),
                    "num list": self.num.tolist()}
        return ret_dict

    def from_dict(self, temp_dict):
        """从字典导入参数

        从外部字典变量导入参数

        :param temp_dict: 参数组成的字典
        :return: 无
        """
        self.id = temp_dict["id"]
        self.name = temp_dict["name"]
        for i in range(96):
            self.type[i] = temp_dict["type list"][i]
        for i in range(96):
            self.num[i] = temp_dict["num list"][i]


class MeasureProcess(object):
    """检测流程类 

    设置该检测流程的类型、参数等信息，并可以存储与读取

    id:编号，保护变量，项目流程列表中的编号。
    type:类型，保护变量
    para:参数，保护变量，根据类型的不同参数内容也不一样
    """

    process_types = ['none', 'measure', 'kinetic', 'door', 'pause']

    def __init__(self):
        self._id = 0
        self._type = 0
        self._para = None

    def __str__(self):
        ret = 'ID:'
        ret += str(self._id) + '\n'
        ret += "TYPE:" + MeasureProcess.process_types[self._type] + \
               '\n'
        ret += "PARA:" + str(self._para)
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
        filter_para = {"du": du, "first filter num": first_filter_num, "second filter num": second_filter_num}
        shake_para = {"strength": shake_strength, "seconds": shake_seconds}
        self._para = {"filter": filter_para, "shake": shake_para}

    def set_process_kinetics(self, id_num,
                             du=1, first_filter_num=2, second_filter_num=4,
                             shake_strength=2, shake_seconds=0,
                             kinetics_times=5, kinetics_minutes=0, kinetics_seconds=5):
        self._id = id_num
        self._type = 2
        filter_para = {"du": du, "first filter num": first_filter_num, "second filter num": second_filter_num}
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
                    time.sleep(self._para["kinetics"]["minutes"] * 60 + self._para["kinetics"]["seconds"])
            print("-----------------")
            print(data_list)

    def to_dict(self):
        ret_dict = {"id": self._id,
                    "type": self._type,
                    "para": self._para}
        return ret_dict

    def from_dict(self, temp_dict):
        self._id = temp_dict["id"]
        self._type = temp_dict["type"]
        self._para = temp_dict["para"]


class MeasureCalculate(object):
    """计算方法类

    定义计算方法的类型、计算参数以及执行计算操作。

    Attributes:
        _id:计算列表中的编号，保护变量
        _type:计算的类型，保护变量
        _para:计算的参数，保护变量
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
        ret += str(self._id) + '\n'
        ret += "TYPE:" + MeasureCalculate.calculate_types[self._type] + \
               '\n'
        ret += "PARA:" + str(self._para)
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
    """测量结果类

    存储测量计算得到的结果

    Attributes:
        id:序号
        time:测量时间
        od_data_current_plate:当前选择的整板OD值。
        od_data_df:所有OD值列表，为DF类型
        _count:OD值板数
        _current:当前OD值板序号
    """

    def __init__(self):
        self.id = 0
        self.time = None
        self._count = 0
        self._current = 0
        header = []
        letter = list(map(chr, range(ord('A'), ord('H') + 1)))
        num = [str(x) for x in range(1, 13)]
        for j in num:
            for i in letter:
                header.append(i + j)
        self.od_data_current_plate = pd.Series(0.0, index=header)
        self.od_data_df = pd.DataFrame(index=header)

    def __str__(self):
        ret = "count:" + str(self._count) + "\n"
        ret += "time:" + str(self.time) + "\n"
        ret += "data:" + str(self.od_data_df) + "\n"
        ret += "current plate data:\n" + str(self._current) + "\n" + str(self.od_data_current_plate)
        return ret

    def __clear_current_data(self):
        for i in range(96):
            self.od_data_current_plate[i] = 0

    def get_plate_od_from_list(self, od_list):
        for i in range(96):
            self.od_data_current_plate[i] = od_list[i]
        self.od_data_df.insert(self.od_data_df.shape[1], str(self.od_data_df.shape[1] + 1), od_list)
        self._count += 1
        self._current = self.od_data_df.shape[1]

    def select_current_plate(self, num):
        if num < self._count + 1:
            self._current = num
            self.od_data_current_plate = self.od_data_df.loc[:, str(self._current)]
            return True
        else:
            self.__clear_current_data()
            return False


class MeasureProject(object):
    """项目设置

    测量项目的内容，参数，流程等进行设置，并可以进行存储。

    Attributes:
        id:项目ID号，值唯一
        name:项目名称
        note:项目说明
        layout:项目布局，为布局类
        process_list:流程列表，为流程类的列表
        calculate_list:计算过程列表，为计算类的列表
        results:结果，为结果类
        reports:# TODO(ayl):待补充
    """

    file_path = "./projects/"
    result_folder = "result"
    layout_folder = "layout"

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
        if mrs_file.check_dir_exist(mrs_file.link_dir(MeasureProject.file_path, str(self.id))):
            print("error")
        else:
            mrs_file.new_folder(MeasureProject.file_path, str(self.id))
            mrs_file.new_folder(mrs_file.link_dir(MeasureProject.file_path, str(self.id)), MeasureProject.layout_folder)
            mrs_file.new_folder(mrs_file.link_dir(MeasureProject.file_path, str(self.id)), MeasureProject.result_folder)
        temp_path = MeasureProject.file_path + str(self.id) + "/" + str(self.id) + ".json"
        temp_st = {"id": self.id,
                   "name": self.name,
                   "note": self.note,
                   "process list": [self.process_list[i].to_dict() for i in range(len(self.process_list))],
                   "calculate list": self.calculate_list}
        with open(temp_path, "w", encoding='utf-8') as f:
            json.dump(temp_st, f, indent=2)

    def load(self, id_num):
        temp_path = MeasureProject.file_path + str(id_num) + "/" + str(id_num) + ".json"
        with open(temp_path, "r", encoding='utf-8') as f:
            temp_st = json.load(f)
        self.id = temp_st["id"]
        self.name = temp_st["name"]
        self.note = temp_st["note"]
        self.process_list = temp_st["process list"]
        self.calculate_list = temp_st["calculate list"]


if __name__ == '__main__':
    """
    aa = MeasureProject()
    bb = MeasureProcess()
    bb.set_process_measure(1)
    aa.process_list.append(bb)
    aa.save()
    """

    aa = MeasureProject()
    aa.load(0)
    print("================")
    print(aa)


