import sys
from PyQt6.QtWidgets import QApplication, QWidget
from ui_form_measure_od import *


class GuiFormMeasureOd(QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(GuiFormMeasureOd, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    """"
    w = QWidget()
    w.resize(250, 200)
    w.move(300, 300)
    w.setWindowTitle('hello')
    w.show()
    """
    gui_form_measure_od = GuiFormMeasureOd()
    gui_form_measure_od.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
