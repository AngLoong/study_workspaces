"任意类型曲线拟合"

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import ast
import math

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
        self.r2 = 0.0
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

    def print_info(self):
        print('A:'+str(self.para_a))
        print('B:'+str(self.para_b))
        print('C:'+str(self.para_c))
        print('D:'+str(self.para_d))
        print('R:'+str(self.r2))

    def func_line(self, x):
        return self.para_a*x+self.para_b

    def func_conic(self,x):
        """
        二次曲线
        """
        return self.para_a* x ** 2 + self.para_b * x + self.para_c

    def func_cubic(self,x):
        """
        三次曲线
        """
        return self.para_a * x ** 3  + self.para_b * x ** 2 + self.para_c * x + self.para_d

    def func_semi_log(self,x):
        """
        半对数
        """
        return self.para_a * np.log(x) + self.para_b

    def func_logit_4p(self, x):
        """
        logit 4P
        """
        return (self.para_a - self.para_d)/(1 + (x/self.para_c)**self.para_b) +self.para_d

    def func_ex1(self, x):
        return self.para_a*np.exp(self.para_b/x)

    def fit_ex1(self):
        def func(x,a,b):
            return a*np.exp(b/x)
        popt, pcov = curve_fit(func, self.axis_x_data, self.axis_y_data)
        self.para_a = popt[0]
        self.para_b = popt[1]
        return

    def fit_line(self):
        def func(x,a,b):
            return a*x+b
        popt, pcov = curve_fit(func,self.axis_x_data, self.axis_y_data)
        self.para_a = popt[0]
        self.para_b = popt[1]
        self.title = str(self.para_a)+'*x+'+str(self.para_b)+'=y'
        y_average = np.average(self.axis_y_data)
        y_curve_value = self.func_line(self.axis_x_data)
        self.r2 = np.sum((y_curve_value - y_average)**2)/np.sum((self.axis_y_data-y_average)**2)
        return

    def fit_conic(self):
        def func(x,a,b,c):
            return a*x*x+b*x+c
        popt, pcov = curve_fit(func,self.axis_x_data, self.axis_y_data)
        self.para_a = popt[0]
        self.para_b = popt[1]
        self.para_c = popt[2]
        self.title = str(self.para_a)+'*x^2+'+str(self.para_b)+'*x+'+str(self.para_c)+'=y'
        y_average = np.average(self.axis_y_data)
        y_curve_value = self.func_conic(self.axis_x_data)
        self.r2 = np.sum((y_curve_value - y_average)**2)/np.sum((self.axis_y_data-y_average)**2)
        return

    def fit_cubic(self):
        def func(x, a, b, c, d):
            return a * x * x * x + b * x * x + c * x + d
        popt, pcov = curve_fit(func,self.axis_x_data,self.axis_y_data)
        self.para_a = popt[0]
        self.para_b = popt[1]
        self.para_c = popt[2]
        self.para_d = popt[3]
        self.title = str(self.para_a)+'*x^3+' + str(self.para_b)+'*x^2+'+str(self.para_c)+'*x+'+str(self.para_d)+'=y'
        y_average = np.average(self.axis_y_data)
        y_curve_value = self.func_cubic(self.axis_x_data)
        self.r2 = np.sum((y_curve_value - y_average)**2)/np.sum((self.axis_y_data-y_average)**2)
        return

    def fit_semi_log(self):
        def func(x, a, b,):
            return a * np.log(x) + b
        popt, pcov = curve_fit(func, self.axis_x_data,self.axis_y_data)
        self.para_a = popt[0]
        self.para_b = popt[1]
        self.title = str(self.para_a) +  '*lnx+' + str(self.para_b) + '=y'
        y_average = np.average(self.axis_y_data)
        y_curve_value = self.func_semi_log(self.axis_x_data)
        self.r2 = np.sum((y_curve_value - y_average)**2)/np.sum((self.axis_y_data-y_average)**2)
        return

    def fit_logit_4p(self):
        def func(x, a, b, c, d):
            return (a - d)/(1 + (x / c) ** b) + d
            #return (a - d)/(1 + pow(x/c,b)) +d
        popt, pcov = curve_fit(func, self.axis_x_data, self.axis_y_data)
        self.para_a = popt[0]
        self.para_b = popt[1]
        self.para_c = popt[2]
        self.para_d = popt[3]
        self.title = "("+str(self.para_a)+"-"+str(self.para_d)+")/(1+(x/"+str(self.para_c)+")^"+str(self.para_b)+")+"+str(self.para_d)+"=y"
        y_average = np.average(self.axis_y_data)
        y_curve_value = self.func_logit_4p(self.axis_x_data)
        self.r2 = np.sum((y_curve_value - y_average)**2)/np.sum((self.axis_y_data-y_average)**2)
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

    def draw_curve_semi_log(self):
        tempx = np.arange(self.axis_x_data[0], self.axis_x_data[-1], (self.axis_x_data[-1] - self.axis_x_data[0])/20.0)
        yvalues = self.func_semi_log(tempx)
        plot = plt.plot(tempx,yvalues,self.curve_color, label = self.curve_label)
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
        elif type == "semi_log":
            self.fit_semi_log()
            self.draw_smp_point()
            self.draw_curve_semi_log()
        elif type == "logit_4p":
            self.fit_logit_4p()
            self.draw_smp_point()
            self.draw_curve_logit_4p()
        else:
            print("other error")
            return -1
        self.print_info()
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
    print('曲线拟合工具')
    x = np.arange(1,17,1)
    y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
    listx = np.array(ast.literal_eval(input("输入x序列，用'，'隔开数据")))
    listy = np.array(ast.literal_eval(input("输入y序列，用','隔开数据")))
    aa = CurveFit(listx,listy)
    typ = input("输入曲线类型：line,conic,cubic,logit_4p,semi_log")
    ret = aa.fit_curve_and_draw_plot(typ)
    if ret < 0:
        print("error")
