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
    count,数据点个数
    axis_x_data,X坐标列表
    axis_y_data,Y坐标列表
    k,方程斜率
    b,方程截距
    r,线性回归系数
    exp,线性方程，poly1d类型
    """

    def __init__(self, list_x, list_y, point_count=6):
        """
        将所有的属性初始化为空白
        """
        self.count = point_count
        self.axis_x_data = list_x
        self.axis_y_data = list_y
        self.k = None
        self.b = None
        self.r = None
        self.exp = None

    def __str__(self):
        res = "x:"+str(self.axis_x_data)+"\ny:"+str(self.axis_y_data)
        res += "\nexp:"+str(self.exp)+"\nr:"+str(self.r)+"\nk:"+str(self.k)+"\nb:"+str(self.b)
        return res

    def __linear_fit(self, order=1):
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

    def __para(self):
        """
        进行线性拟合，并计算r.

        Args:

        Returns:
        计算得到的方程k,b,r

        Raises:

        """
        slope, intercept, r_value, p_value, std_err = stats.linregress(self.axis_x_data, self.axis_y_data)
        return slope, intercept, r_value

    def draw_plot(self):
        """

        :return:无
        """
        plt.scatter(self.axis_x_data, self.axis_y_data, color='blue')
        line_x = [self.axis_x_data[0], self.axis_x_data[self.count-1]]
        line_y = [self.exp(self.axis_x_data[0]), self.exp(self.axis_x_data[self.count-1])]
        plt.plot(line_x, line_y, color='r')
        plt.show()

    def calculate(self, order=1):
        """
        计算
        :param order:拟合方程类型，默认1为线性
        :return: 无
        """
        if len(self.axis_x_data) == len(self.axis_y_data) == self.count:
            self.exp = self.__linear_fit(order)
            self.k, self.b, self.r = self.__para()
            print(self.__str__())
            # self.draw_plot()
            return True
        else:
            return False

    def get_y_value(self, x_value):
        """
        通过x计算y值
        :param x_value:x值
        :return: 结果y值
        """
        return self.exp(x_value)


if __name__ == '__main__':
    linear1 = LinearFit([1, 2, 3, 4, 5, 6], [0.11, 0.23, 0.29, 0.42, 0.50, 0.58], 6)
    # linear1.axis_x_data = [1,2,3,4,5]
    # linear1.axis_y_data = [0.8,1.9,3.0,3.8,5.1]
    linear1.calculate()
    print(linear1.get_y_value(9))
    # print(linear1)
    x = [1,2,3,4,5,6]
    y = [0.8,1.9,3.0,3.8,5.1,6.7]
    # line_x = [1,5]
    # plt.scatter(x,y)
    # plt.plot(line_x,line_y,color='r')
    # plt.show()
