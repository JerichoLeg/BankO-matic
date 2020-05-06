# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMlocop2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_SecondWindow(object):
    
    def atmLocMain(self):
        from atmLocMain import Ui_MainWindow
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def locator(self):
        if (self.enterLocation.text()==""):
            pass
        else:
            a = self.branch2.checkLocation(self.enterLocation.text())
            if (a=="LocationFound"):
                self.branch2.createMap()
                self.webEngineView.setProperty("url", QtCore.QUrl("file:///ATMMap2.html"))
                self.enterLocation.setPlaceholderText("LocationFound")
                self.enterLocation.clear()
        
            elif (a=="TooFar"):
                self.enterLocation.setPlaceholderText("TooFar")
                self.enterLocation.clear()
                
            elif (a=="LocationNotFound"):
                self.enterLocation.setPlaceholderText("LocationNotFound")
                self.enterLocation.clear()

    def setupUi(self, SecondWindow):
        from ATMLocator2 import startLocation
        self.branch2=startLocation()
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(540, 360)
        SecondWindow.setMinimumSize(QtCore.QSize(540, 360))
        SecondWindow.setMaximumSize(QtCore.QSize(540, 360))
        SecondWindow.setMouseTracking(True)
        SecondWindow.setStyleSheet("*{\n"
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
        SecondWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.enterLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.enterLocation.setGeometry(QtCore.QRect(170, 330, 201, 21))
        self.enterLocation.setMinimumSize(QtCore.QSize(181, 0))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(-1)
        self.enterLocation.setFont(font)
        self.enterLocation.setText("")
        self.enterLocation.setReadOnly(False)
        self.enterLocation.setClearButtonEnabled(True)
        self.enterLocation.setObjectName("enterLocation")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(10, 90, 521, 231))
        self.webEngineView.setUrl(QtCore.QUrl("file:///ATMMap2.html"))
        self.webEngineView.setObjectName("webEngineView")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("font: 25 8pt \"Calibri Light\";")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 50, 161, 41))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("font: 25 18pt \"Calibri Light\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, -30, 221, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.searchIcon = QtWidgets.QToolButton(self.centralwidget)
        self.searchIcon.setGeometry(QtCore.QRect(370, 330, 27, 22))
        self.searchIcon.setMouseTracking(True)
        self.searchIcon.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/Downloads/atmLocator/iconfinder_Search_858732.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchIcon.setIcon(icon1)
        self.searchIcon.setObjectName("searchIcon")
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        self.searchIcon.clicked.connect(self.locator)
        self.enterLocation.returnPressed.connect(self.locator)
        self.commandLinkButton.clicked.connect(self.atmLocMain)
        self.commandLinkButton.clicked.connect(SecondWindow.close)
        self.toolButton.clicked.connect(SecondWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "ATM Locator"))
        self.toolButton.setText(_translate("SecondWindow", "..."))
        self.enterLocation.setPlaceholderText(_translate("SecondWindow", "Enter your location"))
        self.commandLinkButton.setText(_translate("SecondWindow", "Back"))
        self.label.setText(_translate("SecondWindow", "ATM Locator"))
        self.searchIcon.setText(_translate("SecondWindow", "..."))

import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
