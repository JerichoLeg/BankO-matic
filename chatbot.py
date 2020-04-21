# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatbot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 360)
        MainWindow.setMinimumSize(QtCore.QSize(540, 360))
        MainWindow.setMaximumSize(QtCore.QSize(540, 360))
        MainWindow.setStyleSheet("*{\n"
"font-family: Akrobat;\n"
"}\n"
"QMainWindow{\n"
"border-image:url(:/images/BG.jpg)\n"
"}\n"
"QToolButton{\n"
"background: transparent\n"
"}\n"
"QPushButton{\n"
"color:#dfdfdf;\n"
"background:#00264d;\n"
"border-radius:20px\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 60, 451, 231))
        self.textBrowser.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 300, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 261, 171))
        self.label.setStyleSheet("image: url(:/images/Logoo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(400, 280, 111, 71))
        self.toolButton_2.setStyleSheet("image: url(:/images/button.png);\n"
"font: 63 12pt \"Akrobat SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 10, 161, 41))
        self.commandLinkButton.setMinimumSize(QtCore.QSize(71, 41))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(9)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BankO\'Matic"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your message"))
        self.toolButton_2.setText(_translate("MainWindow", "Send"))
        self.commandLinkButton.setText(_translate("MainWindow", "Back to Main Menu"))

import res_rc
