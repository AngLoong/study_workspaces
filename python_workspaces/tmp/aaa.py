#!/bin/python

_metaclass_=type #确定使用新式类

pets = ['dog', 'cat', 'bear', 'cat','dog','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

