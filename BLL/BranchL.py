# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'branchLocMain.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets


class Ui_BranchL(object):
    def menu(self):
        from menu import Ui_Menu
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Menu()
        self.ui.setupM(self.window)
        self.window.show()
        
    def openWindow1(self):
        from branchLocOp1 import Ui_Window1
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window1()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def openWindow2(self):
        from branchLocOp2 import Ui_Window2
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Window2()
        self.ui.setupUi(self.window2)
        self.window2.show()
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 360)
        MainWindow.setMinimumSize(QtCore.QSize(540, 360))
        MainWindow.setMaximumSize(QtCore.QSize(540, 360))
        MainWindow.setStyleSheet("*{\n"
"font-family: Calibri Light;\n"
"}\n"
"QMainWindow{\n"
"border-image:url(:/images/BG.jpg)\n"
"}\n"
"QCommandLinkButton{\n"
"font-family: Calibri Light;\n"
"font-size: 12px;\n"
"}\n"
"QCommandLinkButton:hover{\n"
"background: #2E5984;\n"
"border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"font-family: Calibri Light;\n"
"font-size: 30px;\n"
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
"QPushButton:hover{\n"
"background:#2E5984;\n"
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
        self.closeIcon = QtWidgets.QToolButton(self.centralwidget)
        self.closeIcon.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeIcon.setIcon(icon)
        self.closeIcon.setIconSize(QtCore.QSize(50, 50))
        self.closeIcon.setObjectName("closeIcon")
        self.displayText = QtWidgets.QLabel(self.centralwidget)
        self.displayText.setGeometry(QtCore.QRect(160, 130, 221, 31))
        self.displayText.setAlignment(QtCore.Qt.AlignCenter)
        self.displayText.setWordWrap(False)
        self.displayText.setIndent(0)
        self.displayText.setObjectName("displayText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 281, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 145, 31))
        self.commandLinkButton.setMouseTracking(True)
        self.commandLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton.setAutoFillBackground(False)
        self.commandLinkButton.setStyleSheet("")
        self.commandLinkButton.setIconSize(QtCore.QSize(20, 10))
        self.commandLinkButton.setDescription("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 240, 291, 31))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 190, 291, 31))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setObjectName("pushButton")
    
        self.label.raise_()
        self.closeIcon.raise_()
        self.displayText.raise_()
        self.commandLinkButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.openWindow2)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.openWindow1)
        self.pushButton.clicked.connect(MainWindow.close)
        self.commandLinkButton.clicked.connect(self.menu)
        self.commandLinkButton.clicked.connect(MainWindow.close)
        self.closeIcon.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Branch Locator"))
        self.closeIcon.setText(_translate("MainWindow", "..."))
        self.displayText.setText(_translate("MainWindow", "Branch Locator"))
        self.commandLinkButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.pushButton_2.setText(_translate("MainWindow", "Find all nearest branch locations"))
        self.pushButton.setText(_translate("MainWindow", "View all branch locations in the City of Manila"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_BranchL()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
