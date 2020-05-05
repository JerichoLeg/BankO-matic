# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatbot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from menu import *

class Ui_Chatbot(object):
    def menu(self):
        from menu import Ui_Menu
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Menu()
        self.ui.setupM(self.window)
        self.window.show()
        self.MainWindow.close()
        
    def Bot(self):
        if (self.lineEdit.text()==""):
            pass
        else:
            self.listWidget.addItem("You: " + self.lineEdit.text()+"\n") #chat ng tao
            self.listWidget.addItem("Chatbot: " + self.bot.chat(self.lineEdit.text())+"\n")#para sagot ni bot
            self.lineEdit.clear() #para maclear
            self.listWidget.scrollToBottom()
            
    def setupUi(self, MainWindow):
        from Chatbot import botChat
        self.bot=botChat()
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 360)
        MainWindow.setMinimumSize(QtCore.QSize(540, 360))
        MainWindow.setMaximumSize(QtCore.QSize(540, 360))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
"font: 25 8pt \"Calibri Light\";\n"
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 300, 371, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"font: 25 8pt \"Calibri Light\";")
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(400, 280, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("image: url(:/images/button.png);\n"
"font: 25 12pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 10, 161, 41))
        self.commandLinkButton.setMinimumSize(QtCore.QSize(71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("font: 25 9pt \"Calibri Light\";")
        self.commandLinkButton.setIconSize(QtCore.QSize(20, 20))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 60, 461, 231))
        self.listWidget.setStyleSheet("background: transparent;\n"
"font: 25 9pt \"Calibri Light\";\n"
"alternate-background-color: rgb(223, 223, 223);")
        self.listWidget.setAutoScrollMargin(5)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setWordWrap(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 321, 201))
        self.label.setStyleSheet("image: url(:/images/Logoo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, -30, 201, 121))
        self.label_2.setStyleSheet("image: url(:/images/Logo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.listWidget.raise_()
        self.label.raise_()
        self.toolButton.raise_()
        self.lineEdit.raise_()
        self.toolButton_2.raise_()
        self.commandLinkButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolButton_2.clicked.connect(self.Bot)
        self.commandLinkButton.clicked.connect(self.menu)
        self.lineEdit.returnPressed.connect(self.Bot)
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Chatbot()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

