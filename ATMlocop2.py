# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMlocop2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
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
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(180, -10, 181, 121))
        self.label_logo.setStyleSheet("image: url(:/images/Logo.png)")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 181, 41))
        self.commandLinkButton.setMouseTracking(True)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 70, 141, 41))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 110, 381, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 330, 121, 41))
        self.label_2.setObjectName("label_2")
        self.enterLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.enterLocation.setGeometry(QtCore.QRect(150, 300, 201, 21))
        self.enterLocation.setMinimumSize(QtCore.QSize(181, 0))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(-1)
        self.enterLocation.setFont(font)
        self.enterLocation.setText("")
        self.enterLocation.setReadOnly(False)
        self.enterLocation.setClearButtonEnabled(True)
        self.enterLocation.setObjectName("enterLocation")
        self.searchIcon = QtWidgets.QToolButton(self.centralwidget)
        self.searchIcon.setGeometry(QtCore.QRect(350, 300, 21, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/iconfinder_Search_858732.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchIcon.setIcon(icon1)
        self.searchIcon.setIconSize(QtCore.QSize(40, 40))
        self.searchIcon.setCheckable(True)
        self.searchIcon.setObjectName("searchIcon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.commandLinkButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.label.setText(_translate("MainWindow", "ATM Locator"))
        self.label_2.setText(_translate("MainWindow", "ATM Locator"))
        self.enterLocation.setPlaceholderText(_translate("MainWindow", "               Enter your location"))
        self.searchIcon.setText(_translate("MainWindow", "..."))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
