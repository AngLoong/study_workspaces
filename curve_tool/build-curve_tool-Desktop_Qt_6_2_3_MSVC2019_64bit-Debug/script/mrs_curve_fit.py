"任意类型曲线拟合"

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

class CurveFit(object):
    """
    该类对数据进行曲线拟合，曲线类型可以自定义

    Attributes:

    """

    def __init__(self,list_x,list_y):
        self.axis_x_data = list_x
        self.axis_y_data = list_y
        self.para_a = 0.0
        self.para_b = 0.0
        self.para_c = 0.0
        self.para_d = 0.0

    def func_line(self, x):
        return self.a*x+self.b

    def func_conic(self,x):
        """
        二次曲线
        """
        return self.a* x ** 2 + self.b * x + self.c

    def func_cubic(self,x):
        """
        三次曲线
        """
        return self.a * x ** 3  + self.b * x ** 2 + self.c * x + self.d

    def func_logit_4p(self, x):
        """
        logit 4P
        """
        return (self.a - self.d)/(1 + (x/self.c)**self.b) +self.d

    def func_ex1(self, x):
        return self.a*np.exp(self.b/x)

    def fit_ex1(self):
        def func(x,a,b):
            return a*np.exp(b/x)
        popt, pcov = curve_fit(func, self.axis_x_data, self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        return

    def fit_line(self):
        def func(x,a,b):
            return a*x+b
        popt, pcov = curve_fit(func,self.axis_x_data, self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        return

    def fit_conic(self):
        def func(x,a,b,c):
            return a*x*x+b*x+c
        popt, pcov = curve_fit(func,self.axis_x_data, self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        self.c = popt[2]
        return

    def fit_cubic(self):
        def func(x, a, b, c, d):
            return a * x * x * x + b * x * x + c * x + d
        popt, pcov = curve_fit(func,self.axis_x_data,self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        self.c = popt[2]
        self.d = popt[3]
        return

    def fit_logit_4p(self):
        def func(x, a, b, c, d):
            return (a - d)/(1 + (x / c) ** b) + d
        popt, pcov = curve_fit(func, self.axis_x_data, self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        self.c = popt[2]
        self.d = popt[3]
        return

    def draw_smp_point(self, mark, label_str):
        plot = plt.plot(self.axis_x_data, self.axis_y_data, mark, label = label_str)
        return plot

    def draw_curve_ex1(self, color, label_str):
        yvalues = self.func_ex1(self.axis_x_data)
        plot = plt.plot(self.axis_x_data, yvalues, color,label = label_str)
        return plot

    def draw_curve_line(self,color,label_str):
        yvalues = self.func_line(self.axis_x_data)
        plot = plt.plot(self.axis_x_data, yvalues, color,label = label_str)
        return plot

    def draw_curve_conic(self, color, label_str):
        yvalues = self.func_conic(self.axis_x_data)
        plot = plt.plot(self.axis_x_data, yvalues, color, label = label_str)
        return plot

    def draw_curve_cubic(self, color, label_str):
        yvalues = self.func_cubic(self.axis_x_data)
        plot = plt.plot(self.axis_x_data, yvalues, color, label = label_str)
        return plot

    def draw_curve_logit_4p(self, color, label_str):
        yvalues = self.func_logit_4p(self.axis_x_data)
        plot = plt.plot(self.axis_x_data, yvalues, color, label = label_str)
        return plot

    def show_plot(self, title_str):
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.legend(loc = 4)
        plt.title(title_str)
        plt.show()


if __name__ == '__main__':
    x = np.arange(1,17,1)
    y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
    """
    def func(x,a,b):
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
    """
    aa=CurveFit(x,y)
    #aa.fit_ex1()
    #aa.fit_line()
    #aa.fit_conic()
    #aa.fit_cubic()
    aa.fit_logit_4p()
    aa.draw_smp_point('*',"smp")
    #aa.draw_curve_ex1('r','ex1')
    #aa.draw_curve_line('r','line')
    #aa.draw_curve_conic('r','conic')
    #aa.draw_curve_cubic('r','cubic')
    aa.draw_curve_logit_4p('r', 'logit-4p')
    aa.show_plot("figer")



