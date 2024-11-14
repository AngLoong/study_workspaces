#!/bin/python

_metaclass_=type #确定使用新式类

from copy import deepcopy

def test_dict_autoadd():
    dd1 = dict(name="ang",age=18)
    print(dd1)
    dd1['sex'] = 'man'
    print(dd1)

def test_printf():
    dd1 = dict(name="ang",age=18)
    print("name is %(name)s" % dd1)

def test_clear():
    dd1 = dict(name="ang",age=18)
    dd2 = dd1 #dd1 和dd2 为同一个字典的映射
    print(f"=:{dd2}")
    dd1['sex'] = 'man'
    print(f"add sex:{dd2}")
    #dd1 = {}
    #print(f"=blank:{dd2}")
    dd1.clear()
    print(f"clear:{dd2}")

def test_clear2():
    x = {}
    y = x
    x ['key'] = 'value'
    print(f"y:{y}")
    x.clear()
    print(f"y2:{y}")

def test_copy():
    dd1 = {'name':'ang','age':18,'sex':'man','num':[1,2,3],'card':['a','b','c']}
    dd2 = dd1.copy()
    dd1['age'] = 20
    dd1['num'].append(4)
    dd2['sex'] = 'woman'
    dd2['card'].append('d')
    print(f"dd1:{dd1}")
    print(f"dd2:{dd2}")

def test_deepcopy():
    dd1 = {'name':'ang','age':18,'sex':'man','num':[1,2,3],'card':['a','b','c']}
    dd2 = deepcopy(dd1)
    dd1['age'] = 20
    dd1['num'].append(4)
    dd2['sex'] = 'woman'
    dd2['card'].append('d')
    print(f"dd1:{dd1}")
    print(f"dd2:{dd2}")

def test_get():
    dd1 = {}
    print(dd1.get('name')) #>>>None
    print(dd1.get('name','N/A')) #>>>N/A
    print(dd1['name']) #>>>KeyError 

def test_items():
    dd1 = {'name':'ang','age':18,'sex':'man','num':[1,2,3],'card':['a','b','c']}
    ll1 = dd1.items()
    print(f"items:{ll1}")

def test_setdefault():
    dd1 = {}
    print(dd1.setdefault('name'))
    print(dd1)
    dd1['name'] = 'ang'
    print(dd1.setdefault('name'))
    print(dd1)
    print(dd1.setdefault('age','N/A'))
    print(dd1)


if __name__ == '__main__':
    test_setdefault()

