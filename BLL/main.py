# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from log import lgn
from PyQt5 import QtWebEngineWidgets
from Chatbot import botChat
import os

#Clear function
if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

class Ui_Login(object):
    def regwin(self):
        from register import Ui_Register
        self.window = QtWidgets.QDialog()
        self.ui=Ui_Register()
        self.ui.setupR(self.window)
        self.window.show()
        
    def menu(self):
        from menu import Ui_Menu
        self.window =QtWidgets.QDialog()
        self.ui=Ui_Menu()
        self.ui.setupM(self.window)
        self.window.show()
    
    def log(self):
        a = self.log1.checkAccount(self.userfield1.text(),self.passfield1.text())
        if(a=="correct"):
            self.Login.close()
            self.menu()
        elif(a == "incorrect"):
            self.statuscheck.setText("Password is incorrect")
        else:
            self.statuscheck.setText("User does not exist")
            

    def setupL(self, Login):
        self.log1 = lgn()
        cb = botChat()
        clear()
        self.Login=Login
        Login.setObjectName("Login")
        Login.resize(540, 360)
        Login.setMinimumSize(QtCore.QSize(540, 360))
        Login.setMaximumSize(QtCore.QSize(540, 360))
        Login.setStyleSheet("*{\n"
"font-family: Calibri Light;\n"
"}\n"
"QDialog{\n"
"border-image:url(:/images/bgm1.png)\n"
"}\n"
"QToolButton{\n"
"background: transparent\n"
"}\n"
"QPushButton{\n"
"color:#dfdfdf;\n"
"background:#004285;\n"
"border-radius:10px\n"
"}\n"
"QFrame{\n"
"background:rgba(22, 37, 75, 0.94);\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"color:#dfdfdf;\n"
"background: transparent;\n"
"}\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"background: #dfdfdf;\n"
"}\n"
"QPushButton:Hover{\n"
"color:black;\n"
"background:#dfdfdf;\n"
"border-radius:10px\n"
"}")
        self.toolButton = QtWidgets.QToolButton(Login)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(30, 20, 271, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.loginbutton1 = QtWidgets.QPushButton(self.frame)
        self.loginbutton1.setGeometry(QtCore.QRect(20, 220, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(13)
        self.loginbutton1.setFont(font)
        self.loginbutton1.setObjectName("loginbutton1")
        self.userfield1 = QtWidgets.QLineEdit(self.frame)
        self.userfield1.setGeometry(QtCore.QRect(30, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.userfield1.setFont(font)
        self.userfield1.setObjectName("userfield1")
        self.passfield1 = QtWidgets.QLineEdit(self.frame)
        self.passfield1.setGeometry(QtCore.QRect(30, 170, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.passfield1.setFont(font)
        self.passfield1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passfield1.setObjectName("passfield1")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(-30, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(-30, 130, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.statuscheck = QtWidgets.QLabel(self.frame)
        self.statuscheck.setGeometry(QtCore.QRect(30, 260, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(9)
        self.statuscheck.setFont(font)
        self.statuscheck.setText("")
        self.statuscheck.setAlignment(QtCore.Qt.AlignCenter)
        self.statuscheck.setObjectName("statuscheck")
        self.toolButton_2 = QtWidgets.QToolButton(Login)
        self.toolButton_2.setGeometry(QtCore.QRect(300, 70, 241, 201))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(900, 900))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_5 = QtWidgets.QLabel(Login)
        self.label_5.setGeometry(QtCore.QRect(40, 320, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.regbutton = QtWidgets.QPushButton(Login)
        self.regbutton.setGeometry(QtCore.QRect(180, 320, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(8)
        self.regbutton.setFont(font)
        self.regbutton.setObjectName("regbutton")

        self.retranslateUi(Login)
        self.loginbutton1.clicked.connect(self.log)
        self.toolButton.clicked.connect(Login.close)
        self.regbutton.clicked.connect(self.regwin)
        self.regbutton.clicked.connect(Login.close)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.toolButton.setText(_translate("Login", "..."))
        self.label.setText(_translate("Login", "Welcome!"))
        self.label_2.setText(_translate("Login", "Login to your account"))
        self.loginbutton1.setText(_translate("Login", "LOGIN"))
        self.userfield1.setPlaceholderText(_translate("Login", " your username"))
        self.passfield1.setPlaceholderText(_translate("Login", " *****"))
        self.label_3.setText(_translate("Login", "Username :"))
        self.label_4.setText(_translate("Login", "Password :"))
        self.toolButton_2.setText(_translate("Login", "..."))
        self.label_5.setText(_translate("Login", "Don\'t have an account?"))
        self.regbutton.setText(_translate("Login", "Sign-up here"))


import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupL(Login)
    Login.show()
    sys.exit(app.exec_())

