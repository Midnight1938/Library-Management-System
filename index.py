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
    ### Show things ###
        self.Show_Authors()
        self.Show_Category()
        self.Show_Publishers()
    ### Show CBB Things ###
        self.Show_Category_CBB()
        self.Show_Author_CBB()
        self.Show_Publisher_CBB()

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

        Book_name = self.lineEdit_3.text()
        Book_describe = self.textEdit.toPlainText()
        Book_code = self.lineEdit_4.text()
        Book_category = self.comboBox_3.currentIndex()
        Book_author = self.comboBox_4.currentIndex()
        Book_publisher = self.comboBox_5.currentIndex()
        Book_price = self.lineEdit_5.text()
        
        self.cur.execute('''
                         INSERT INTO Book(Book_name , Book_describe , Book_code , Book_category, Book_author, Book_publisher, Book_price)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)
                         ''', (Book_name , Book_describe , Book_code , Book_category, Book_author, Book_publisher, Book_price))

        self.db.commit()
        self.statusBar().showMessage("New Book added")
        
        self.lineEdit_3.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_4.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_5.setText('')
        
    def Search_Book(self):
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

####### ** ----------------- ** #######
####### ** Tweaks tab Things ** #######
####### ** ----------------- ** #######
### !! Categories !! ###
    def Add_Category(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
                         INSERT INTO Categories (Category_name) VALUES (%s)
                         ''', (category_name,))
        self.db.commit()
        self.lineEdit_19.setText('')
        self.statusBar().showMessage("Category added Succesfully")
        self.Show_Category()
        self.Show_Category_CBB()

### *Showing categories* ###
    def Show_Category(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM Categories ''')
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
                         INSERT INTO Authors (Author_name) VALUES (%s)
                         ''', (author_name,))
        self.db.commit()
        self.lineEdit_20.setText('')
        self.statusBar().showMessage("Author Added Succesfully")
        self.Show_Authors()
        self.Show_Author_CBB()

### *Showing Authors* ###
    def Show_Authors(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM Authors ''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(
                        row, column, QTableWidgetItem(str(item)))
                    column += 1

                Row_Position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(Row_Position)


### !! Publishers !! ###


    def Add_Publisher(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()

        self.cur.execute('''
                         INSERT INTO Publishers (Publisher_name) VALUES (%s)
                         ''', (publisher_name,))
        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage("Publisher added Succesfully")
        self.Show_Publishers()
        self.Show_Publisher_CBB()

### *Showing Publishers* ###
    def Show_Publishers(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM Publishers ''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(
                        row, column, QTableWidgetItem(str(item)))
                    column += 1

                Row_Position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(Row_Position)


####### ** ---------------- ** #######
####### **   UI Settings    ** #######
####### ** ---------------- ** #######

    def Show_Category_CBB(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM Categories ''')
        data = self.cur.fetchall()
        
        self.comboBox_3.clear()
        for category in data:
            self.comboBox_3.addItem(category[0])


    def Show_Author_CBB(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM Authors ''')
        data = self.cur.fetchall()
        
        self.comboBox_4.clear()
        for category in data:
            self.comboBox_4.addItem(category[0])


    def Show_Publisher_CBB(self):
        self.db = pymysql.connect(
            host='localhost', user='root', password='Password123#@', db='Library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM Publishers ''')
        data = self.cur.fetchall()
        
        self.comboBox_5.clear()
        for category in data:
            self.comboBox_5.addItem(category[0])



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
