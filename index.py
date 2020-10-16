from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql
pymysql.install_as_MySQLdb()

ui, _ = loadUiType('Library.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()
        self.Show_Category()

    def Handle_UI_Changes(self):
        self.Hiding_Theme()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        ## ** For Themes ** ##
        self.pushButton_5.clicked.connect(self.Show_Theme)
        self.pushButton_21.clicked.connect(self.Hiding_Theme)
    ## ** For Navigation ** ##
        self.pushButton.clicked.connect(self.Open_Daily_Manage)
        self.pushButton_2.clicked.connect(self.Open_Books)
        self.pushButton_3.clicked.connect(self.Open_Users)
        self.pushButton_4.clicked.connect(self.Open_Tweaks)
    ## ** For Books ** ##
        self.pushButton_7.clicked.connect(self.Add_New_Book)
    ## ** Adding Categories ** ##
        self.pushButton_14.clicked.connect(self.Add_Category)
    ## ** Adding Author ** ##
        self.pushButton_15.clicked.connect(self.Add_Author)
    ## ** Adding Publisher ** ##
        self.pushButton_16.clicked.connect(self.Add_Publisher)

####### ** ---------------- ** #######
####### **  Theme Tweaking  ** #######
####### ** ---------------- ** #######
    def Show_Theme(self):
        self.groupBox_3.show()

    def Hiding_Theme(self):
        self.groupBox_3.hide()

####### ** ---------------- ** #######
####### ** Tabs to navigate ** #######
####### ** ---------------- ** #######
    def Open_Daily_Manage(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books(self):
        pass
        self.tabWidget.setCurrentIndex(1)

    def Open_Users(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Tweaks(self):
        pass
        self.tabWidget.setCurrentIndex(3)

####### ** ---------------- ** #######
####### **   Books Stuff    ** #######
####### ** ---------------- ** #######
    def Add_New_Book(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        book.title = self.lineEdit_3.text()
        book.code = self.lineEdit_4.text()
        book.category = self.comboBox_3.CurrentText()
        book.author = self.comboBox_4.CurrentText()
        book.publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_5.text()

    def Saerch_Book(self):
        pass

    def Edit_Book(self):
        pass

    def Remove_Book(self):
        pass

####### ** ---------------- ** #######
####### **   Users Stuff    ** #######
####### ** ---------------- ** #######
    def Add_User(self):
        pass

    def Login_User(self):
        pass

    def Edit_User_Info(self):
        pass

####### ** ---------------- ** #######
####### **   Tweaks Stuff   ** #######
####### ** ---------------- ** #######

### !! Categories !! ###
    def Add_Category(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
                         INSERT INTO Category (Category_name) VALUES (%s)
                         ''', (category_name,))
        self.db.commit()
        self.statusBar().showMessage("Category added Succesfully")
        self.lineEdit_19.setText('')
        self.Show_Category()

### *Showing categories* ###
    def Show_Category(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM Category ''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(
                        row, column, QTableWidgetItem(str(item)))
                    column += 1

                Row_Position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(Row_Position)

### !! Authors !! ###
    def Add_Author(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()

        self.cur.execute('''
                         INSERT INTO Author (Author_name) VALUES (%s)
                         ''', (author_name,))
        self.db.commit()
        self.statusBar().showMessage("Author Added Succesfully")
        self.lineEdit_20.setText('')

### *Showing Authors* ###
    def Show_Authors(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()


### !! Publishers !! ###

    def Add_Publisher(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()

        self.cur.execute('''
                         INSERT INTO Publisher (Publisher_name) VALUES (%s)
                         ''', (publisher_name,))
        self.db.commit()
        self.statusBar().showMessage("Publisher added Succesfully")
        self.lineEdit_21.setText('')

### *Showing Publishers* ###
    def Show_Publishers(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()


####### !! ---------------- !! #######
####### **  Program Runner  ** #######
####### !! ---------------- !! #######


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
