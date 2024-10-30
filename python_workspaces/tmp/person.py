#!/bin/python

_metaclass_=type #确定使用新式类

class Person:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("hello,world!I'm %s." % self.name)

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
