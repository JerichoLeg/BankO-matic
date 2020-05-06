# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def chatb(self):
        from BotChatG import Ui_Chatbot
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_Chatbot()
        self.ui.setupUi(self.window)
        self.window.show()
        self.Menu.close()

    def branchl(self):
        from BranchL import Ui_BranchL
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_BranchL()
        self.ui.setupUi(self.window)
        self.window.show()
        self.Menu.close()
        
    def atml(self):
        from atmLocMain import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.Menu.close()
      
    def setupM(self, Menu):
        self.Menu=Menu
        Menu.setObjectName("Menu")
        Menu.resize(540, 360)
        Menu.setMinimumSize(QtCore.QSize(540, 360))
        Menu.setMaximumSize(QtCore.QSize(540, 360))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        Menu.setFont(font)
        Menu.setStyleSheet("*{\n"
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
"background:#00264d;\n"
"border-radius:10px\n"
"}\n"
"QFrame{\n"
"background:rgba(22, 37, 75, 0.94);\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"color:black;\n"
"background: transparent;\n"
"}\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"background: #dfdfdf;\n"
"}\n"
"QPushButton:Hover{\n"
"color:black;\n"
"background:#004d99;\n"
"border-radius:10px\n"
"}")
        self.toolButton = QtWidgets.QToolButton(Menu)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Menu)
        self.toolButton_2.setGeometry(QtCore.QRect(280, 80, 241, 201))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(900, 900))
        self.toolButton_2.setObjectName("toolButton_2")
        self.brnch = QtWidgets.QPushButton(Menu)
        self.brnch.setGeometry(QtCore.QRect(30, 110, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        self.brnch.setFont(font)
        self.brnch.setObjectName("brnch")
        self.atm = QtWidgets.QPushButton(Menu)
        self.atm.setGeometry(QtCore.QRect(30, 180, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        self.atm.setFont(font)
        self.atm.setObjectName("atm")
        self.chatbot = QtWidgets.QPushButton(Menu)
        self.chatbot.setGeometry(QtCore.QRect(30, 250, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        self.chatbot.setFont(font)
        self.chatbot.setObjectName("chatbot")
        self.label = QtWidgets.QLabel(Menu)
        self.label.setGeometry(QtCore.QRect(40, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.toolButton_3 = QtWidgets.QToolButton(Menu)
        self.toolButton_3.setGeometry(QtCore.QRect(40, 120, 31, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons8-bank-building-64 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(Menu)
        self.toolButton_4.setGeometry(QtCore.QRect(40, 190, 31, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons8-atm-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(Menu)
        self.toolButton_5.setGeometry(QtCore.QRect(40, 260, 41, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons8-chat-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_5.setObjectName("toolButton_5")

        self.retranslateUi(Menu)
        self.brnch.clicked.connect(self.branchl)
        self.atm.clicked.connect(self.atml)
        self.chatbot.clicked.connect(self.chatb)
        self.toolButton.clicked.connect(Menu.close)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.toolButton.setText(_translate("Menu", "..."))
        self.toolButton_2.setText(_translate("Menu", "..."))
        self.brnch.setText(_translate("Menu", "  Branch Locator"))
        self.atm.setText(_translate("Menu", "ATM Locator"))
        self.chatbot.setText(_translate("Menu", "Chatbot"))
        self.label.setText(_translate("Menu", "MENU"))
        self.toolButton_3.setText(_translate("Menu", "..."))
        self.toolButton_4.setText(_translate("Menu", "..."))
        self.toolButton_5.setText(_translate("Menu", "..."))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupM(Menu)
    Menu.show()
    sys.exit(app.exec_())

