"""
关于软件设置的文件
"""


import numpy as np
import pandas as pd
import json


class ConfigProperty(object):
    """

    """

    attributes = {}

    def __init__(self):
        # self.attributes = {}
        pass

    def __str__(self):
        ret = str(ConfigProperty.attributes)
        return ret

    @classmethod
    def reset(cls):
        path_data_export = "./"
        filter_setting = {"1": "405", "2": "450", "3": "492", "4": "630", "5": "",
                          "6": "", "7": "", "8": "", "9": "", "10": "",
                          "11": "", "12": "", "13": "", "14": "", "15": ""}
        serial_setting = {"com": "COM6",
                          "baud": 115200,
                          "time out": None}
        cls.attributes = {"data path": path_data_export,
                          "filter settings": filter_setting,
                          "serial settings": serial_setting}

    @classmethod
    def save(cls):
        with open("./config.json", "w", encoding='utf-8') as f:
            json.dump(ConfigProperty.attributes, f, indent=2)

    @classmethod
    def load(cls):
        with open("./config.json", "r", encoding='utf-8') as f:
            ConfigProperty.attributes = json.load(f)


if __name__ == '__main__':
    cc = ConfigProperty()
    print("cc:", cc)
    # cc.reset()
    # cc.save()
    cc.load()
    print("cc:", cc)
    dd = ConfigProperty()
    print("dd:", dd)
    print("com:", dd.attributes["serial settings"]["com"])
