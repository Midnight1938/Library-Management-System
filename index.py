from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from xlrd import *
import datetime
import sys
import pymysql


ui, _ = loadUiType('Library.ui')
login,_ = loadUiType('Login.ui')

####### !! ---------------- !! #######
####### !!  Login Windows   !! #######
####### !! ---------------- !! #######
class Login(QWidget,login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Loginer)

    def Loginer(self):
        Username = self.lineEdit.text()
        Password = self.lineEdit_2.text()

        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()


        sql = ''' SELECT * FROM Users'''

        self.cur.execute(sql)
        Data = self.cur.fetchall()
        for row in Data:
            if Username == row[1] and Password == row[3]:
                self.label.setText("Logging In")
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText("Username or Password is incorrect")
                
####### !! ---------------- !! #######
####### !!   Main Windows   !! #######
####### !! ---------------- !! #######
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
    ### Showing Clients ###
        self.Show_Clients()
        self.Show_Books()

    ### Operations ###
        self.Show_Operation()
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
        self.pushButton_26.clicked.connect(self.Open_Clients)
    ## ** For Books ** ##
        self.pushButton_7.clicked.connect(self.Add_New_Book)
    ## ** Adding Categories ** ##
        self.pushButton_14.clicked.connect(self.Add_Category)
    ## ** Adding Author ** ##
        self.pushButton_15.clicked.connect(self.Add_Author)
    ## ** Adding Publisher ** ##
        self.pushButton_16.clicked.connect(self.Add_Publisher)
    ## ** Editing Book info ** ##
        self.pushButton_9.clicked.connect(self.Search_Books)
        self.pushButton_8.clicked.connect(self.Edit_Book)
        self.pushButton_10.clicked.connect(self.Remove_Book)
    ## ** Adding Users ** ##
        self.pushButton_11.clicked.connect(self.Add_User)
        self.pushButton_12.clicked.connect(self.Login_User)
        self.pushButton_13.clicked.connect(self.Edit_User_Info)
    ## ** Stuff with Clients ** ##
        self.pushButton_22.clicked.connect(self.Add_New_Client)
        self.pushButton_24.clicked.connect(self.Search_Clients)
        self.pushButton_23.clicked.connect(self.Edit_Clients)
        self.pushButton_25.clicked.connect(self.Delete_Clients)
    ## ** USING themes ** ##
        self.pushButton_17.clicked.connect(self.Black_theme)
        self.pushButton_18.clicked.connect(self.BreezeDrk_theme)
        self.pushButton_19.clicked.connect(self.DrkOrange_theme)
        self.pushButton_20.clicked.connect(self.Navy_theme)
    ## ** Day-to-Day ** ##
        self.pushButton_6.clicked.connect(self.Daily_Operations)

####### ** ---------------- ** #######
####### ** Top_Bar Tweaking ** #######
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
        self.tabWidget.setCurrentIndex(3)

    def Open_Clients(self):
        pass
        self.tabWidget.setCurrentIndex(2)

    def Open_Tweaks(self):
        pass
        self.tabWidget.setCurrentIndex(4)

####### ** ---------------- ** #######
####### !! Day-To-Day Stuff !! #######
####### ** ---------------- ** #######
    def Show_Operation(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()
        
        self.cur.execute('''
                         SELECT Book_name, Client, Type, Duration, To_date from Daily_Tasks
                         ''')
        data = self.cur.fetchall()
        
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    def Daily_Operations(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Book_title = self.lineEdit.text()
        Client = self.lineEdit_29.text()
        Type = self.comboBox.currentText()
        Duration = self.comboBox_2.currentIndex() + 1
        Cur_Date = datetime.date.today()
        To_date = Cur_Date + datetime.timedelta(days=Duration) 

        print(Cur_Date)
        print(To_date)
        
        self.cur.execute('''
                         INSERT INTO Daily_Tasks(book_name, client, type, duration, date, to_date )
                         VALUES (%s, %s, %s, %s, %s, %s)
                         ''', (Book_title, Client, Type, Duration, Cur_Date, To_date))
        
        self.db.commit()
        self.Show_Operation()
        self.statusBar().showMessage("Book Logged Sucessfully")
        

####### ** ---------------- ** #######
####### **   Books Stuff    ** #######
####### ** ---------------- ** #######

    def Show_Books(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute(
            ''' SELECT Book_code, Book_name, Book_describe, Book_category, Book_author, Book_publisher, Book_price FROM Book ''')
        data = self.cur.fetchall()
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(
                    row, column, QTableWidgetItem(str(item)))
                column += 1

            Row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(Row_position)
        self.db.close()

    def Add_New_Book(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Book_name = self.lineEdit_3.text()
        Book_describe = self.textEdit.toPlainText()
        Book_code = self.lineEdit_4.text()
        Book_category = self.comboBox_3.currentText()
        Book_author = self.comboBox_4.currentText()
        Book_publisher = self.comboBox_5.currentText()
        Book_price = self.lineEdit_5.text()

        self.cur.execute('''
                         INSERT INTO Book(Book_name , Book_describe , Book_code , Book_category, Book_author, Book_publisher, Book_price)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)
                         ''', (Book_name, Book_describe, Book_code, Book_category, Book_author, Book_publisher, Book_price))

        self.db.commit()
        self.statusBar().showMessage("New Book added")

        self.lineEdit_3.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_4.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_5.setText('')
        self.Show_Books()

    def Search_Books(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_7.text()

        sql = (''' SELECT * FROM Book WHERE book_name = %s ''')
        self.cur.execute(sql, [(book_title)])

        data = self.cur.fetchone()
        ### Data defined ###
        self.lineEdit_6.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_9.setText(data[3])
        self.comboBox_6.setCurrentText(data[4])
        self.comboBox_7.setCurrentText(data[5])
        self.comboBox_8.setCurrentText(data[6])
        self.lineEdit_8.setText(str(data[7]))

    def Edit_Book(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Book_name = self.lineEdit_6.text()
        Book_describe = self.textEdit_2.toPlainText()
        Book_code = self.lineEdit_9.text()
        Book_category = self.comboBox_6.currentText()
        Book_author = self.comboBox_7.currentText()
        Book_publisher = self.comboBox_8.currentText()
        Book_price = self.lineEdit_8.text()

        search_book_title = self.lineEdit_7.text()

        self.cur.execute('''
                         UPDATE Book SET Book_name=%s, Book_describe=%s, Book_code=%s, Book_category=%s, Book_author=%s, Book_publisher=%s, Book_price=%s WHERE book_name = %s
                         ''', (Book_name, Book_describe, Book_code, Book_category, Book_author, Book_publisher, Book_price, search_book_title))

        self.db.commit()
        self.statusBar().showMessage("Book Info Updated")
        self.Show_Books()

    def Remove_Book(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_7.text()

        warning = QMessageBox.warning(
            self, 'Delete Book', 'Are you sure you want to delete this??', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            sql = ''' DELETE FROM Book WHERE Book_name = %s '''
            self.cur.execute(sql, [(book_title)])
            self.db.commit()
            self.statusBar().showMessage("Book removed")
        self.Show_Books()

####### ** ---------------- ** #######
####### **   Client Stuff   ** #######
####### ** ---------------- ** #######
    def Show_Clients(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute(
            ''' SELECT client_ID, client_email, client_name FROM Clients ''')
        data = self.cur.fetchall()
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(
                    row, column, QTableWidgetItem(str(item)))
                column += 1

            Row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(Row_position)
        self.db.close()

    def Add_New_Client(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Client_name = self.lineEdit_22.text()
        Client_email = self.lineEdit_24.text()
        Client_ID = self.lineEdit_23.text()

        self.cur.execute('''
                         INSERT INTO Clients (client_name, client_email, client_ID)
                         VALUES(%s,%s,%s)
                         ''', (Client_name, Client_email, Client_ID))
        self.db.commit()
        self.db.close()
        self.lineEdit_22.setText('')
        self.lineEdit_24.setText('')
        self.statusBar().showMessage("Client added successfully")
        self.Show_Clients()

    def Search_Clients(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Client_ID = self.lineEdit_26.text()

        sql = '''SELECT * FROM Clients WHERE Client_ID = %s '''
        self.cur.execute(sql, [(Client_ID)])
        data = self.cur.fetchone()

        self.lineEdit_28.setText(data[1])
        self.lineEdit_27.setText(data[2])
        self.lineEdit_25.setText(data[3])

    def Edit_Clients(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Client_init_ID = self.lineEdit_25.text()
        Client_name = self.lineEdit_28.text()
        Client_email = self.lineEdit_27.text()
        Client_ID = self.lineEdit_26.text()

        self.cur.execute('''
                         UPDATE Clients SET Client_name = %s,Client_email = %s,Client_ID = %s WHERE Client_ID = %s
                         ''', (Client_name, Client_email, Client_ID, Client_init_ID))
        self.db.commit()
        self.statusBar().showMessage('Client Data Updated')
        self.lineEdit_25.setText('')
        self.lineEdit_28.setText('')
        self.lineEdit_27.setText('')
        self.db.close()
        self.Show_Clients()

    def Delete_Clients(self):
        Client_original_ID = self.lineEdit_25.text()

        warning_message = QMessageBox.warning(
            self, 'Delete client', 'Are you sure you want to delete this Client?', QMessageBox.Yes | QMessageBox.No)

        if warning_message == QMessageBox.Yes:

            self.db = pymysql.connect(
                host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
            self.cur = self.db.cursor()

            sql = '''DELETE FROM Clients WHERE Client_ID = %s'''
            self.cur.execute(sql, [(Client_original_ID)])

            self.db.commit()
            self.statusBar().showMessage('Client Deleted')
            self.lineEdit_25.setText('')
            self.lineEdit_28.setText('')
            self.lineEdit_27.setText('')
            self.db.close()
            self.Show_Clients()

####### ** ---------------- ** #######
####### **   Users Stuff    ** #######
####### ** ---------------- ** #######

    def Add_User(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Username = self.lineEdit_2.text()
        Email = self.lineEdit_10.text()
        Password = self.lineEdit_11.text()
        Re_Pass = self.lineEdit_12.text()

        if Password == Re_Pass:
            self.cur.execute('''
                             INSERT INTO Users(user_name, user_email, user_password)
                             VALUES (%s,%s,%s)
                             ''', (Username, Email, Password))

            self.db.commit()
            self.label_30.setText("User Added Sucessfully")

        else:
            self.label_30.setText("Passwords dont match")

    def Login_User(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        Username = self.lineEdit_13.text()
        Password = self.lineEdit_14.text()

        sql = ''' SELECT * FROM Users'''

        self.cur.execute(sql)
        Data = self.cur.fetchall()
        for row in Data:
            if Username == row[1] and Password == row[3]:
                print('user matched')
                self.statusBar().showMessage("User Found")
                self.groupBox_4.setEnabled(True)

                self.lineEdit_17.setText(row[1])
                self.lineEdit_15.setText(row[2])
                self.lineEdit_16.setText(row[3])

            else:
                self.statusBar().showMessage("User Not Found")

    def Edit_User_Info(self):

        Username = self.lineEdit_15.text()
        Email = self.lineEdit_16.text()
        Password = self.lineEdit_17.text()
        Re_Password = self.lineEdit_18.text()

        if Password == Re_Password:
            self.db = pymysql.connect(
                host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
            self.cur = self.db.cursor()

            self.cur.execute('''
                             UPDATE Users SET user_name= %s, user_email= %s, user_password= %s WHERE user_name= %s
                             ''', (Username, Email, Password, Username))
            self.db.commit()
            self.statusBar().showMessage('User Info Updated')
            self.label_31.setText("Info Updated")

        else:
            self.label_31.setText("Passwords dont match")

####### ** ----------------- ** #######
####### ** Tweaks tab Things ** #######
####### ** ----------------- ** #######
    ### !! Categories !! ###
    def Add_Category(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
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
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute('''
                         SELECT category_name FROM Categories
                         ''')
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
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
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
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute('''
                         SELECT author_name FROM Authors
                         ''')
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
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
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
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute('''
                         SELECT publisher_name FROM Publishers
                         ''')
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
####### ** Book UI Settings ** #######
####### ** ---------------- ** #######

    def Show_Category_CBB(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute('''
                         SELECT category_name FROM Categories
                         ''')
        data = self.cur.fetchall()

        self.comboBox_3.clear()
        for category in data:
            self.comboBox_3.addItem(category[0])
            self.comboBox_6.addItem(category[0])

    def Show_Author_CBB(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute('''
                         SELECT author_name FROM Authors
                         ''')
        data = self.cur.fetchall()

        self.comboBox_4.clear()
        for category in data:
            self.comboBox_4.addItem(category[0])
            self.comboBox_7.addItem(category[0])

    def Show_Publisher_CBB(self):
        self.db = pymysql.connect(
            host='remotemysql.com', user='sK2s1bWndE', password='ocnTQrgalf', db='sK2s1bWndE')
        self.cur = self.db.cursor()

        self.cur.execute('''
                         SELECT publisher_name FROM Publishers
                         ''')
        data = self.cur.fetchall()

        self.comboBox_5.clear()
        for category in data:
            self.comboBox_5.addItem(category[0])
            self.comboBox_8.addItem(category[0])


####### ** ---------------- ** #######
####### ??    UI Themes     ?? #######
####### ** ---------------- ** #######

    def Black_theme(self):
        style = open('Themes/Black.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def BreezeDrk_theme(self):
        style = open('Themes/Breeze_dark_style.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def DrkOrange_theme(self):
        style = open('Themes/DrkOrange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Navy_theme(self):
        style = open('Themes/Navy.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

####### !! ---------------- !! #######
####### **  Program Runner  ** #######
####### !! ---------------- !! #######


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
