# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMlocop1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_FirstWindow(object):
    def atmLocMain(self):
        from atmLocMain import Ui_MainWindow
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, FirstWindow):
        from ATMLocator import create
        create()
        self.FirstWindow = FirstWindow
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(540, 360)
        FirstWindow.setMinimumSize(QtCore.QSize(540, 360))
        FirstWindow.setMaximumSize(QtCore.QSize(540, 360))
        FirstWindow.setMouseTracking(True)
        FirstWindow.setStyleSheet("*{\n"
"font-family: Calibri Light;\n"
"}\n"
"QMainWindow{\n"
"border-image:url(:/images/BG.jpg)\n"
"}\n"
"QLabel{\n"
"font-family: Calibri Light;\n"
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
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(10, 90, 521, 261))
        self.webEngineView.setStyleSheet("")
        self.webEngineView.setUrl(QtCore.QUrl("file:///ATMMap1.html"))
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
        self.label.setGeometry(QtCore.QRect(200, 50, 161, 41))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("font: 25 18pt \"Calibri Light\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, -30, 221, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        FirstWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstWindow)
        self.commandLinkButton.clicked.connect(self.atmLocMain)
        self.commandLinkButton.clicked.connect(FirstWindow.close)
        self.toolButton.clicked.connect(FirstWindow.close)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "ATM Locator"))
        self.toolButton.setText(_translate("FirstWindow", "..."))
        self.commandLinkButton.setText(_translate("FirstWindow", "Back"))
        self.label.setText(_translate("FirstWindow", "ATM Locator"))

import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    sys.exit(app.exec_())
