#!/bin/python

_metaclass_=type #确定使用新式类

from dog import Dog

class BigDog(Dog): #括号中为指定父类
    """一次模拟大型小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        super().__init__(name,age) #super()函数调用父类的__init__()方法，从而让子类继承父类的所有属性。
        self.weight = 20 #子类的属性
    
    def eat(self):
        print(self.name.title() + " is eating.") #子类的方法
    
    def roll_over(self):    # 重新定义父类的方法
        print("big dog: " + self.name.title() + " rolled over!")

if __name__ == '__main__' :
    aaa = BigDog('John',3)
    aaa.eat()
    aaa.roll_over()


