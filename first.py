import sys, math

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLCDNumber


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Желтые кружочки')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = Window()
    wd.show()
    sys.exit(app.exec())