import sys, math

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLCDNumber


class Window(QMainWindow):
    global a, b
    def __init__(self):
        self.a = ""
        self.b = ""
        super(Window, self).__init__()
        uic.loadUi('calc.ui', self)
        self.setWindowTitle('Красивый калькулятор')
        self.btn0.clicked.connect(self.bt0_click)
        self.btn1.clicked.connect(self.bt1_click)
        self.btn2.clicked.connect(self.bt2_click)
        self.btn3.clicked.connect(self.bt3_click)
        self.btn4.clicked.connect(self.bt4_click)
        self.btn5.clicked.connect(self.bt5_click)
        self.btn6.clicked.connect(self.bt6_click)
        self.btn7.clicked.connect(self.bt7_click)
        self.btn8.clicked.connect(self.bt8_click)
        self.btn9.clicked.connect(self.bt9_click)
        self.btn_clear.clicked.connect(self.bt_clear_click)
        self.btn_div.clicked.connect(self.bt_div_click)
        self.btn_fact.clicked.connect(self.bt_fact_click)
        self.btn_minus.clicked.connect(self.bt_minus_click)
        self.btn_mult.clicked.connect(self.bt_mult_click)
        self.btn_dot.clicked.connect(self.bt_dot_click)
        self.btn_eq.clicked.connect(self.bt_eq_click)
        self.btn_pow.clicked.connect(self.bt_pow_click)
        self.btn_sqrt.clicked.connect(self.bt_sqrt_click)
        self.btn_plus.clicked.connect(self.bt_plus_click)

    def bt0_click(self):
        if self.a == "0":
            self.a = "0"
            self.table.display(self.a)
        else:
            self.a += "0"
            self.table.display(self.a)

    def bt1_click(self):
        self.a += "1"
        self.table.display(self.a)

    def bt2_click(self):
        self.a += "2"
        self.table.display(self.a)

    def bt3_click(self):
        self.a += "3"
        self.table.display(self.a)

    def bt4_click(self):
        self.a += "4"
        self.table.display(self.a)

    def bt5_click(self):
        self.a += "5"
        self.table.display(self.a)

    def bt6_click(self):
        self.a += "6"
        self.table.display(self.a)

    def bt7_click(self):
        self.a += "7"
        self.table.display(self.a)

    def bt8_click(self):
        self.a += "8"
        self.table.display(self.a)

    def bt9_click(self):
        self.a += "9"
        self.table.display(self.a)

    def bt_clear_click(self):
        self.a = ""
        self.b = ""
        self.table.display(self.a)

    def bt_div_click(self):
        if self.b == "":
            self.b = self.a + "/"
            self.a = ""

    def bt_fact_click(self):
        self.table.display(math.factorial(int(self.a)))
        self.a = ""

    def bt_plus_click(self):
        self.b = self.a + "+"
        self.a = ""



    def bt_minus_click(self):
        if self.a == "":
            self.a += "-"
        else:
            self.b = self.a + "-"
            self.a = ""
        self.table.display(self.a)

    def bt_mult_click(self):
        if self.b == "":
            self.b = self.a + "*"
            self.a = ""

    def bt_dot_click(self):
        if self.a.find(".") == -1:
            self.a += "."


    def bt_eq_click(self):
        self.b += self.a
        self.a = eval(self.b)
        self.table.display(self.a)
        self.b = ""
        self.a = ""


    def bt_pow_click(self):
        self.a += "**"
        self.b = self.a
        self.a = ""


    def bt_sqrt_click(self):
        if self.b == "":
            print(self.a)
            if eval(self.a) < 0:
                self.table.display("Error")
            else:
                self.table.display(math.sqrt(eval(self.a)))
        else:
            if eval(self.b) < 0:
                if eval(self.a) < 0:
                    self.table.display("Error")
            else:
                self.table.display(math.sqrt(eval(self.b)))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = Window()
    wd.show()
    sys.exit(app.exec())

