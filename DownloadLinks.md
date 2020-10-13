# Get things installed in Linux

## Install QTDesigner, SQL Workbench

wget -c <https://build-system.fman.io/static/public/files/Qt%20Designer%20Setup.exe>

wget -c <https://cdn.mysql.com//Downloads/MySQLGUITools/mysql-workbench-community_8.0.21-1ubuntu20.04_amd64.deb>
* * *

## SQL Functions

sudo apt install mysql-server
    - For More info
    [visit LikeGeeks](https://likegeeks.com/mysql-on-linux-beginners-tutorial/)

## Edit zshrc or bashrc to make running QT Designer easy

**In terminal**
gedit ~/.zshrc (or bashrc if you dont use OhMyZsh)
**Add at the bottom line, Or in the Alias Section in zshrc**
alias Qtdes="wine /home/<--YOURUSERNAME-->/.wine/drive_c/Program\ Files\ \(x86\)/Qt\ Designer/designer.exe"
