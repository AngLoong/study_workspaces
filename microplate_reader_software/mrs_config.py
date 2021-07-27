"""
关于软件设置的文件
"""


import numpy as np
import pandas as pd
import json


class ConfigProperty(object):
    """

    """

    def __init__(self):
        self.attributes = {}

    def __str__(self):
        ret = str(self.attributes)
        return ret

    def reset(self):
        path_data_export = "./"
        filter_setting = {"1": "405", "2": "450", "3": "492", "4": "630", "5": "", \
                          "6": "", "7": "", "8": "", "9": "", "10": "", \
                          "11": "", "12": "", "13": "", "14": "", "15": ""}
        self.attributes = {"data path": path_data_export, \
                           "filter settings": filter_setting}

    def save(self):
        with open("./config.json", "w", encoding='utf-8') as f:
            json.dump(self.attributes, f, indent=2)

    def load(self):
        with open("./config.json","r",encoding='utf-8') as f:
            self.attributes = json.load(f)

if __name__ == '__main__':
    cc = ConfigProperty()
    #print(cc)
    #cc.save()
    cc.load()
    print(cc)