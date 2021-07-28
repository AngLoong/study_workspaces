"""
交互界面控制
"""


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

import ui_main
import ui_project_attributes


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ui_main.Ui_Main()
    ui.ui.show()
    sys.exit(app.exec())
