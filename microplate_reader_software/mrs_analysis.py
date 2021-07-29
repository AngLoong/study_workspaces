"""
分析仪器性能参数
"""


import numpy as np
import pandas as pd


def ana_stability(data):
    df = pd.DataFrame()

    row = df.loc["A1"]
    row_max = max(row)
    row_min = min(row)
    print(row_max)
    print(row_min)