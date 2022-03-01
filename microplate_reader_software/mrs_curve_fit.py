"任意类型曲线拟合"

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

class CurveFit(object):
    """
    该类对数据进行曲线拟合，曲线类型可以自定义

    Attributes:

    """

    def __init__(self,list_x,list_y,curve_type):
        self.axis_x_data = list_x
        self.axis_y_data = list_y

    def func_line(x,k,b):
        return k*x+b


if __name__ == '__main__':
    x = np.arange(1,17,1)
    y = np.array([4.00,6.40,8.00,8.80,9.22,9.05,9.70,9.86,10.00,10.20,10.32,10.42,10.50,10.58,10.60])
    def func(x,a,b)
        return a*np.exp(b/x)
    popt, pcov = curve_fit(func, x, y)
    a = popt[0]
    b = popt[1]
    yvals = func(x,a,b)
    plot1 = plt.plot(x,y,'*',label = 'original values')
    plot2 = plt.plot(x,yvals,'r',label = 'curve_fit values')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.legend(loc=4)
    plt.title('curve_fit')
    plt.show()
    plt.savefig('p2.png')
