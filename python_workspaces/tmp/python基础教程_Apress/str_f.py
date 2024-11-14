#!/bin/python

_metaclass_=type #确定使用新式类

from string import Template


def test_printf():
	format = "hello, %s,%s enough fo ya?"
	values1 = ('world','Hot')
	print(format % values1)

def test_template():
	template = Template('$x, glorious $x!,Yo$x.It is ${x}tastic')
	str = template.substitute(x='slurm')
	print(str)
	template2 = Template('A $thing must never $action')
	d = {}
	d['thing'] = 'gentleman'
	d['action'] = 'show his socks'
	str = template2.substitute(d)
	print(str)

def test_printf_1():
	ff1 = "%.*s"
	val = (5,'Guido van Rossum')
	print(ff1 % val)

def test_join():
	se1 = ['a','b','c']
	se2 = '-'
	ss = se2.join(se1) #>>>abc-abc-abc
	print(ss)

def test_replace():
	str1 = "this is a pig"
	str2 = str1.replace('is','is not')
	print(f"str1:{str1}")
	print(f"str2:{str2}")

def test_split():
    ss1 = '1+2+3+4+5'
    ll1 = ss1.split('+')
    print(f"ss1:{ss1}")
    print(f"ll1:{ll1}")

def test_translate():
    table = str.maketrans('cs','kz')
    print(table)
    print(len(table))
    str1 = "a cat is sleeping"
    str2 = str1.translate(table)
    print(str1)
    print(str2)

if __name__ == '__main__':
    test_translate()


