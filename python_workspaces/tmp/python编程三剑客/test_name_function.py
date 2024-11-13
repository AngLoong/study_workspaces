#!/bin/python

_metaclass_=type #确定使用新式类

import unittest

from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function"""
    """
    def __init__(self):
        super().__init__()
    """
    def test_first_last_name(self):
        """测试"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """测试middlename"""
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__' :
    unittest.main()

