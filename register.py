# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
from menu import *
class Ui_Register(object):
    def loginwin(self):
        self.window = QtWidgets.QDialog()
        self.ui=Ui_Login()
        self.ui.setupL(self.window)
        self.window.show()
    def setupR(self, Register):
        Register.setObjectName("Register")
        Register.resize(540, 360)
        Register.setMinimumSize(QtCore.QSize(540, 360))
        Register.setMaximumSize(QtCore.QSize(540, 360))
        Register.setStyleSheet("*{\n"
"font-family: Akrobat;\n"
"}\n"
"QDialog{\n"
"border-image:url(:/images/BG.jpg)\n"
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
        self.toolButton = QtWidgets.QToolButton(Register)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(20, 10, 271, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.signup = QtWidgets.QPushButton(self.frame)
        self.signup.setGeometry(QtCore.QRect(30, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(13)
        self.signup.setFont(font)
        self.signup.setObjectName("signup")
        self.userfield = QtWidgets.QLineEdit(self.frame)
        self.userfield.setGeometry(QtCore.QRect(30, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(12)
        self.userfield.setFont(font)
        self.userfield.setObjectName("userfield")
        self.passfield = QtWidgets.QLineEdit(self.frame)
        self.passfield.setGeometry(QtCore.QRect(30, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(12)
        self.passfield.setFont(font)
        self.passfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passfield.setObjectName("passfield")
        self.usernametext = QtWidgets.QLabel(self.frame)
        self.usernametext.setGeometry(QtCore.QRect(40, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(10)
        self.usernametext.setFont(font)
        self.usernametext.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernametext.setObjectName("usernametext")
        self.emailtext = QtWidgets.QLabel(self.frame)
        self.emailtext.setGeometry(QtCore.QRect(40, 130, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(10)
        self.emailtext.setFont(font)
        self.emailtext.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.emailtext.setObjectName("emailtext")
        self.emailfield = QtWidgets.QLineEdit(self.frame)
        self.emailfield.setGeometry(QtCore.QRect(30, 160, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(12)
        self.emailfield.setFont(font)
        self.emailfield.setObjectName("emailfield")
        self.passtext = QtWidgets.QLabel(self.frame)
        self.passtext.setGeometry(QtCore.QRect(40, 200, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(10)
        self.passtext.setFont(font)
        self.passtext.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passtext.setObjectName("passtext")
        self.cancel = QtWidgets.QPushButton(self.frame)
        self.cancel.setGeometry(QtCore.QRect(140, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(13)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.toolButton_2 = QtWidgets.QToolButton(Register)
        self.toolButton_2.setGeometry(QtCore.QRect(300, 70, 241, 201))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(900, 900))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(Register)
        self.signup.clicked.connect(self.loginwin)
        self.cancel.clicked.connect(self.loginwin)
        self.toolButton.clicked.connect(Register.close)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.toolButton.setText(_translate("Register", "..."))
        self.label.setText(_translate("Register", "Create Account"))
        self.signup.setText(_translate("Register", "Sign Up"))
        self.userfield.setPlaceholderText(_translate("Register", " your username"))
        self.passfield.setPlaceholderText(_translate("Register", " *****"))
        self.usernametext.setText(_translate("Register", "Username :"))
        self.emailtext.setText(_translate("Register", "Email :"))
        self.emailfield.setPlaceholderText(_translate("Register", " your@email.com"))
        self.passtext.setText(_translate("Register", "Password :"))
        self.cancel.setText(_translate("Register", "Cancel"))
        self.toolButton_2.setText(_translate("Register", "..."))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupR(Register)
    Register.show()
    sys.exit(app.exec_())

