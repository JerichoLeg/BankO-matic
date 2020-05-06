# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'branchLocOp1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_Window1(object):
    def BranchL(self):
        from BranchL import Ui_BranchL
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_BranchL()
        self.ui.setupUi(self.window)
        self.window.show()

        
    def setupUi(self, Window1):
        from BranchLocator1 import create 
        create()
        self.Window1=Window1
        Window1.setObjectName("Window1")
        Window1.resize(540, 360)
        Window1.setMinimumSize(QtCore.QSize(540, 360))
        Window1.setMaximumSize(QtCore.QSize(540, 360))
        Window1.setMouseTracking(True)
        Window1.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(Window1)
        self.centralwidget.setObjectName("centralwidget")
        self.closeIcon = QtWidgets.QToolButton(self.centralwidget)
        self.closeIcon.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeIcon.setIcon(icon)
        self.closeIcon.setIconSize(QtCore.QSize(50, 50))
        self.closeIcon.setObjectName("closeIcon")
        self.displayText = QtWidgets.QLabel(self.centralwidget)
        self.displayText.setGeometry(QtCore.QRect(180, 60, 171, 21))
        self.displayText.setAlignment(QtCore.Qt.AlignCenter)
        self.displayText.setWordWrap(False)
        self.displayText.setIndent(0)
        self.displayText.setObjectName("displayText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, -40, 201, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.commandLinkButton.setMouseTracking(True)
        self.commandLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton.setAutoFillBackground(False)
        self.commandLinkButton.setStyleSheet("")
        self.commandLinkButton.setIconSize(QtCore.QSize(20, 10))
        self.commandLinkButton.setDescription("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(10, 90, 521, 261))
        self.webEngineView.setProperty("url", QtCore.QUrl("file:///BranchMap1.html"))
        self.webEngineView.setObjectName("webEngineView")
        self.label.raise_()
        self.closeIcon.raise_()
        self.displayText.raise_()
        self.commandLinkButton.raise_()
        self.webEngineView.raise_()
        Window1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window1)
        self.commandLinkButton.clicked.connect(self.BranchL)
        self.commandLinkButton.clicked.connect(Window1.close)
        self.closeIcon.clicked.connect(Window1.close)
        QtCore.QMetaObject.connectSlotsByName(Window1)

    def retranslateUi(self, Window1):
        _translate = QtCore.QCoreApplication.translate
        Window1.setWindowTitle(_translate("Window1", "Branch Locator"))
        self.closeIcon.setText(_translate("Window1", "..."))
        self.displayText.setText(_translate("Window1", "Branch Locator"))
        self.commandLinkButton.setText(_translate("Window1", "Back "))

import res_rc
#from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window1 = QtWidgets.QMainWindow()
    ui = Ui_Window1()
    ui.setupUi(Window1)
    Window1.show()
    sys.exit(app.exec_())
