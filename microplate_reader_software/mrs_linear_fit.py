"""
最小二乘法进行曲线计算
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d
from scipy import stats


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


def function_rsquared(x, y):
    """
    进行线性拟合，并计算R2.

    Args:
        x,x轴数据列表
        y,y轴数据列表

    Returns:
        计算得到的方程k,b,r,R2

    Raises:

    """
    slope,intercept,r_value,p_value,std_err = stats.linregress(x,y)
    return (slope,intercept,r_value,r_value**2)


x = [1,2,3,4,5]
y = [0.8,1.9,3.0,3.8,5.1]
fun_exp = function_get_liner_exp(x,y)
print(fun_exp)
fun_exp2 = function_rsquared(x,y)
print("fun_exp2:y=",fun_exp2[0],"*x+",fun_exp2[1],"   r=",fun_exp2[2],"   R2=",fun_exp2[3])
line_x = [1,5]
line_y = [fun_exp(1),fun_exp(5)]
plt.scatter(x,y)
plt.plot(line_x,line_y,color='r')
plt.show()
