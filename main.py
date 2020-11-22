import sys, random

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    global Ris
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Желтые кружки')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for _ in range(random.randint(0, 12)):
            qp.setBrush(QColor(254, 254, 2))
            a = random.randint(0, 75)
            qp.drawEllipse(random.randint(0, 361), random.randint(0, 254), a, a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = Window()
    wd.show()
    sys.exit(app.exec())
