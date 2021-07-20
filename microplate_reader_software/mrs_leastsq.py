"""
最小二乘法进行曲线计算
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d


def function_get_liner_exp(x, y):
    """
    计算y值

    Args:
        x,x轴数据列表
        y,y轴数据列表

    Returns:
        计算得到的方程k和b值

    Raises:

    """
    fun_para = polyfit(x,y,1)
    return poly1d(fun_para)


x = [1,2,3,4,5]
y = [0.8,1.9,3.0,3.8,5.1]
fun_exp = function_get_liner_exp(x,y)
print(fun_exp)
line_x = [1,5]
line_y = [fun_exp(1),fun_exp(5)]
plt.scatter(x,y)
plt.plot(line_x,line_y,color='r')
plt.show()
