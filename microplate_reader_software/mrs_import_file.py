"""
导入文件
"""

import numpy as ny
import pandas as pd

tb = pd.read_csv("./text.csv")
print(tb)
print(len(tb))
print(tb.info())