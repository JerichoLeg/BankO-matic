# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMlocmain.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_MainWindow(object):

    def menu(self):
        from menu import Ui_Menu
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Menu()
        self.ui.setupM(self.window)
        self.window.show()

        
    def openWindow(self):
        from atmLocOp1 import Ui_FirstWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FirstWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        from atmLocOp2 import Ui_SecondWindow
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(540, 360)
        MainWindow.setMinimumSize(QtCore.QSize(540, 360))
        MainWindow.setMaximumSize(QtCore.QSize(540, 360))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("*{\n"
"font-family: Akrobat;\n"
"}\n"
"QMainWindow{\n"
"border-image:url(:/images/BG.jpg)\n"
"}\n"
"QLabel{\n"
"font-family: Akrobat;\n"
"font-size: 22px;\n"
"}\n"
"QToolButton{\n"
"background: transparent\n"
"}\n"
"QToolButton:hover{\n"
"background: #E0ECF8;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton{\n"
"color:#dfdfdf;\n"
"background:#00264d;\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"background: #dfdfdf;\n"
"font-size:15px;\n"
"}\n"
"QLineEdit:hover{\n"
"border-radius:10px;\n"
"background: #ffffff;\n"
"}\n"
"Qlabel{\n"
"color:#dfdfdf;\n"
"background:transparent;\n"
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 110, 161, 41))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("font: 25 18pt \"Calibri Light\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 170, 321, 41))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("font: 25 10pt \"Calibri Light\";")
        self.pushButton.setObjectName("pushButton")


        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 220, 321, 41))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet("font: 25 10pt \"Calibri Light\";")
        self.pushButton_2.setObjectName("pushButton_2")



        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("font: 25 8pt \"Calibri Light\";")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 0, 281, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.openWindow2)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.commandLinkButton.clicked.connect(self.menu)
        self.commandLinkButton.clicked.connect(MainWindow.close)
        self.toolButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATM Locator"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "ATM Locator"))
        self.pushButton.setText(_translate("MainWindow", "View all ATM locations in the City of Manila"))
        self.pushButton_2.setText(_translate("MainWindow", "Find the nearest ATM locations"))
        self.commandLinkButton.setText(_translate("MainWindow", "Back to Main Menu"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
