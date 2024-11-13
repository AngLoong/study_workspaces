#!/bin/python

_metaclass_=type #确定使用新式类

def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的名字"""
    if middle_name : 
        full_name = f"{first_name} {middle_name} {last_name}"
    else :
        full_name = f"{first_name} {last_name}"
    return full_name.title()


if __name__ == '__main__' :
    pass

