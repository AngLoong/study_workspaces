#!/bin/python

_metaclass_=type #确定使用新式类


fruits = ["Apple", "banana", "Cherry", "date"]
fruits_a = fruits[:]
fruits_a.sort(key=len)
print(f"key=len:>>> {fruits_a}")  # 输出: ['date', 'apple', 'cherry', 'banana']
fruits_b = fruits[:]
fruits_b.sort(key=str.lower)
print(f"key=str.lower:>>> {fruits_b}")  # 输出: ['date', 'apple', 'cherry', 'banana']
fruits_c = fruits[:]
fruits_c.sort()
print(f"default:>>> {fruits_c}")  # 输出: ['date', 'apple', 'cherry', 'banana']

