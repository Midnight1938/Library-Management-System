# Library Management System

- Run on a Cloud-based MySQL
- Built on Python3

[Management structure](https://github.com/Midnight1938/Library-Management/blob/master/MgmntStr.md)
</br>
[Building your own Library: (read)](https://github.com/Midnight1938/Library-Management/blob/master/BuildSQL.md)

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

## Requirements

> ***Install Python3***
<br>

> ***QtDesigner (If you want to edit the .ui files ie the actual LOOK or LAYOUT)***
<br>
>
>> **Install on Windows**
>> <br>
>> https://build-system.fman.io/static/public/files/Qt%20Designer%20Setup.exe
>> <br>
>
>> **Install on Mac**
>> <br>
>> https://build-system.fman.io/static/public/files/Qt%20Designer.dmg
>> <br>
 >
>> **Install on Linux (Debian)**
>> <br>
>
>> ```sudo apt-get install qttools5-dev-tools```
>> <br>
>> ```sudo apt-get install qttools5-dev```

### To install python dependencies, open terminal in this folder and run

```pip install -r requirements.txt```

#### How to put up your own icons:
- Keep the same name (for ease)
- In the folder, open terminal and run:
```pyrcc5 icons.qrc -o icons_rc.py```
