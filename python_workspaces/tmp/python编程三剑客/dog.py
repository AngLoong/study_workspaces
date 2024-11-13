#!/bin/python

_metaclass_=type #确定使用新式类

class Dog: #首字母大写一般约定为类名
    """一次模拟小狗的简单尝试""" #此处对类进行描述
    def __init__(self,name,age): # init 初始化方法，在创建新实例时执行， self形参必不可少
        """初始化属性name和age"""
        self.name = name
        self.age = age  #属性
        self.food = "meat" #带默认值的属性

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


if __name__ == '__main__' :
    aaa = Dog('john',2)
    aaa.sit()


