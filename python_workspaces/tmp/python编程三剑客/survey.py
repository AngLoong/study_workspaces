#!/bin/python

_metaclass_=type #确定使用新式类

class AnonymousSurvey:
    """收集问卷调查问卷的答案"""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """在屏幕上显示问题"""
        print(self.question)

    def store_response(self, response):
        """存储一个答案"""
        self.responses.append(response)
    
    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


if __name__ == '__main__' :
    pass

