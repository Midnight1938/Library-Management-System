from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql
pymysql.install_as_MySQLdb()
from PyQt5.uic import loadUiType

ui, _ = loadUiType('Library.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Hiding_Theme()


    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Theme)
        self.pushButton_21.clicked.connect(self.Hiding_Theme)

    def Show_Theme(self):
        self.groupBox_3.show()

    def Hiding_Theme(self):
        self.groupBox_3.hide()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()