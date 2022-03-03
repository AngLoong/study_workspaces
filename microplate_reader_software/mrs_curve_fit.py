"任意类型曲线拟合"

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import ast

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
        self.smp_plot_shape = '*'
        self.curve_color = 'r'
        self.smp_label = 'smp'
        self.curve_label = 'curve1'
        self.title = ""

    def check_data(self):
        if len(self.axis_x_data) != len(self.axis_y_data):
            return -1
        elif len(self.axis_x_data) < 4:
            return -1
        else:
            return 0

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
        self.title = str(self.a)+'*x+'+str(self.b)+'=y'
        return

    def fit_conic(self):
        def func(x,a,b,c):
            return a*x*x+b*x+c
        popt, pcov = curve_fit(func,self.axis_x_data, self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        self.c = popt[2]
        self.title = str(self.a)+'*x^2+'+str(self.b)+'*x+'+str(self.c)+'=y'
        return

    def fit_cubic(self):
        def func(x, a, b, c, d):
            return a * x * x * x + b * x * x + c * x + d
        popt, pcov = curve_fit(func,self.axis_x_data,self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        self.c = popt[2]
        self.d = popt[3]
        self.title = str(self.a)+'*x^3+' + str(self.b)+'*x^2+'+str(self.c)+'*x+'+str(self.d)+'=y'
        return

    def fit_logit_4p(self):
        def func(x, a, b, c, d):
            return (a - d)/(1 + (x / c) ** b) + d
        popt, pcov = curve_fit(func, self.axis_x_data, self.axis_y_data)
        self.a = popt[0]
        self.b = popt[1]
        self.c = popt[2]
        self.d = popt[3]
        self.title = "("+str(self.a)+"-"+str(self.d)+")/(1+(x/"+str(self.c)+")^"+str(self.b)+")+"+str(self.d)+"=y"
        return

    def draw_smp_point(self):
        plot = plt.plot(self.axis_x_data, self.axis_y_data, self.smp_plot_shape, label = self.smp_label)
        return plot

    def draw_curve_ex1(self):
        yvalues = self.func_ex1(self.axis_x_data)
        plot = plt.plot(self.axis_x_data, yvalues, self.curve_color,label = self.curve_label)
        return plot

    def draw_curve_line(self):
        yvalues = self.func_line(self.axis_x_data)
        plot = plt.plot(self.axis_x_data, yvalues, self.curve_color,label = self.curve_label)
        return plot

    def draw_curve_conic(self):
        tempx =np.arange(self.axis_x_data[0],self.axis_x_data[-1], (self.axis_x_data[-1]-self.axis_x_data[0])/20.0)
        yvalues = self.func_conic(tempx)
        plot = plt.plot(tempx, yvalues, self.curve_color, label = self.curve_label)
        return plot

    def draw_curve_cubic(self):
        tempx =np.arange(self.axis_x_data[0],self.axis_x_data[-1], (self.axis_x_data[-1]-self.axis_x_data[0])/20.0)
        yvalues = self.func_cubic(tempx)
        plot = plt.plot(tempx, yvalues, self.curve_color, label = self.curve_label)
        return plot

    def draw_curve_logit_4p(self):
        tempx =np.arange(self.axis_x_data[0],self.axis_x_data[-1], (self.axis_x_data[-1]-self.axis_x_data[0])/20.0)
        yvalues = self.func_logit_4p(tempx)
        plot = plt.plot(tempx, yvalues, self.curve_color, label = self.curve_label)
        return plot

    def show_plot(self):
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.legend(loc = 4)
        plt.title(self.title)
        plt.show()
        return

    def fit_curve_and_draw_plot(self, type):
        if self.check_data() < 0:
            print("data error")
            return -2
        if type == "line":
            self.fit_line()
            self.draw_smp_point()
            self.draw_curve_line()
        elif type == "conic":
            self.fit_conic()
            self.draw_smp_point()
            self.draw_curve_conic()
        elif type == "cubic":
            self.fit_cubic()
            self.draw_smp_point()
            self.draw_curve_cubic()
        elif type == "logit_4p":
            self.fit_logit_4p()
            self.draw_smp_point()
            self.draw_curve_logit_4p()
        else:
            print("other error")
            return -1
        self.show_plot()
        return 0


if __name__ == '__main__':
    """
    x = np.arange(1,17,1)
    y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
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
    """
    """
    listx = np.array
    listy = np.array
    listx = ast.literal_eval(input("输入x序列，用'，'隔开数据"))
    print(listx)
    listy = ast.literal_eval(input("输入y序列，用','隔开数据"))
    print(listy)
    typ = input("输入曲线类型：line,conic,cubic,logit_4p")
    aa = CurveFit(listx,listy)
    ret = aa.fit_curve_and_draw_plot(typ)
    if ret < 0:
        print("error")
    """
    x = np.arange(1,17,1)
    y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
    listx = np.array(ast.literal_eval(input("输入x序列，用'，'隔开数据")))
    listy = np.array(ast.literal_eval(input("输入y序列，用','隔开数据")))
    aa = CurveFit(listx,listy)
    typ = input("输入曲线类型：line,conic,cubic,logit_4p")
    ret = aa.fit_curve_and_draw_plot(typ)
    if ret < 0:
        print("error")
