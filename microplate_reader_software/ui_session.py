"""
会话界面
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from ui_project_attributes import Ui_ProjectAttributes

class Ui_Session(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800,600)
