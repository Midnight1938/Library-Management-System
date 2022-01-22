#+title: Computer Practical Project 2021
#+description: Project documentation for Computer
#+author: Saksham Sharma
#+SETUPFILE: export/setup/theme-darksun-local.setup
#+date: <2021-09-22 Wed>

[[https://midnight1938.github.io/Library-Management-System/][https://raw.githubusercontent.com/Midnight1938/Library-Management-System/master/Builders/visit-site.svg]]

*Name:* Library Management system

*Version:* 1.4

[[https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg]] [[https://forthebadge.com/images/badges/0-percent-optimized.svg]] [[https://forthebadge.com/images/badges/designed-in-etch-a-sketch.svg]]
[[https://forthebadge.com/images/badges/made-with-python.svg]] [[https://forthebadge.com/images/badges/powered-by-qt.svg]] 

** Overview
Following is a document listing the features of a Library Management System that was built after being frustrated by the manual handling of data at the local library. The features include a system to manage a database of books, Admins and Clients, and the ability to modify, sort and export relevant data.
The document also includes basic instructions if one wants to modify the program

** Objective
 To Build a Library management system that is easy to use and provides a hassel free experience
- Built with [[https://www.python.org/][Python]] and [[https://www.qt.io/][QT Framework]]
  + Python Modules:
    * wheel
    * pyqt5
    * pymysql
    * xlrd
    * xlsxwriter
    * datetime
- MySQL Database Hosted on [[https://clever-cloud.com/en/][Clever Cloud]] with IP Authentication
*** Releases
- Pre-Alpha:

** Features
*** Main system
  - Login Page
  - Users
  - Add Users (Signup)
  - Add a Book
  - Edit Book Info
  - Delete Book
  - Categories
  - Settings [Categs, Author, Publisher]
  - Day To Day Transaction Log
  - Reports [Excel Files]

*** Book
  - Title
  - ISBN Code
  - Description
  - Category
  - Price
  - Author
  - Publisher

*** Admin
  - User Name
  - Password
  - Email Id

*** Client / Students
  - Username
  - Student ID
  - Email ID

*** Day-to-Day
  - Book name
  - Type (Issue / Return)
  - Duration (weeks)

*** Category, Publisher, Author
  - Names
  - List

** Future Prospects
- WebApp
- Integrate barcode scanning
- Ability to select local or cloud database

** Resources
*** Requirements

**** QtDesigner
If you want to edit the .ui files ie the actual LOOK or LAYOUT
+ [[https://build-system.fman.io/static/public/files/Qt%20Designer%20Setup.exe][Install on Windows]]
+ [[https://build-system.fman.io/static/public/files/Qt%20Designer.dmg][Install on Mac]]
+ *Installing on Linux (Debian and Fedora)*
 - [[https://flathub.org/apps/details/io.qt.QtCreator][Flatpak]]
 #+BEGIN_SRC bash
 sudo apt-get install qttools5-dev-tools qttools5-dev
 
 sudo dnf install qttools5-dev-tools qttools5-dev
 #+END_SRC

**** Python Dependencies
To install python dependencies use the =requirements.txt= file with python pip

*** Icon Manipulation:
Follow these steps to change hte programs icons
1. Keep the same name (for ease)
2. In the folder, open terminal and run the following code
   #+BEGIN_SRC bash
   pyrcc5 icons.qrc -o icons_rc.py
   #+END_SRC
