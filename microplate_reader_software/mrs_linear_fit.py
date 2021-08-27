"""
最小二乘法进行曲线计算
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d
from scipy import stats


class LinearFit(object):
    """
    该类对数据进行线性拟合

    Attributes:
    data,原始数据，DataFrame二维表
    r,线性回归系数
    exp,线性方程，poly1d类型
    """

    # data = pd.DataFrame()
    # r = 0
    # exp = np.poly1d()

    def __init__(self, list_x, list_y, point_count=6):
        """
        将所有的属性初始化为空白
        """
        self.count = point_count
        self.axis_x_data = list_x
        self.axis_y_data = list_y
        self.r = None
        self.exp = None

    def __str__(self):
        res = "x:"+str(self.axis_x_data)+"\ny:"+str(self.axis_y_data)
        res += "\nexp:"+str(self.exp)+"\nr:"+str(self.r)
        return res

    def __linear_fit(self,order=1):
        """
        计算线性拟合的公式

        Args:
        order,多项式的阶数，默认1阶，即线性

        Returns:
        拟合的多项式，poly1d类型
        Raises:

        """

        fun_para = polyfit(self.axis_x_data, self.axis_y_data, order)
        return poly1d(fun_para)

    def __rsquared(self):
        """
        进行线性拟合，并计算R2.

        Args:
        x,x轴数据列表
        y,y轴数据列表

        Returns:
        计算得到的方程k,b,r,R2

        Raises:

        """
        slope, intercept, r_value, p_value, std_err = stats.linregress(self.axis_x_data, self.axis_y_data)
        return r_value

    def draw_plot(self):
        plt.scatter(self.axis_x_data, self.axis_y_data, color='blue')
        line_x = [self.axis_x_data[0], self.axis_x_data[self.count-1]]
        line_y = [self.exp(self.axis_x_data[0]), self.exp(self.axis_y_data[self.count-1])]
        plt.plot(line_x, line_y, color='r')
        plt.show()

    def calculate(self, order=1):
        if len(self.axis_x_data) == len(self.axis_y_data) == self.count:
            self.exp = self.__linear_fit(order)
            self.r = self.__rsquared()
            print(self.__str__())
            self.draw_plot()
            return True
        else:
            return False


if __name__ == '__main__':
    linear1 = LinearFit([1, 2, 3, 4, 5], [0.8, 1.9, 3.0, 3.8, 5.1], 5)
    # linear1.axis_x_data = [1,2,3,4,5]
    # linear1.axis_y_data = [0.8,1.9,3.0,3.8,5.1]
    linear1.calculate()
    # print(linear1)
    x = [1,2,3,4,5]
    y = [0.8,1.9,3.0,3.8,5.1]
    # line_x = [1,5]
    # plt.scatter(x,y)
    # plt.plot(line_x,line_y,color='r')
    # plt.show()
