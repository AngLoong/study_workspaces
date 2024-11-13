#!/bin/python

_metaclass_=type #确定使用新式类

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """测试AnonymousSurvey类"""
    def setUp(self):
        """在每个测试方法开始前执行"""
        question = "What's your favorite color?"
        self.my_survey = AnonymousSurvey(question)
        self.response = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.response[0])
        self.assertIn(self.response[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.response:
            self.my_survey.store_response(response)
        for response in self.response:
            self.assertIn(response,self.my_survey.responses)

if __name__ == '__main__' :
    unittest.main()

