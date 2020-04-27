# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMlocop1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(540, 360)
        FirstWindow.setMinimumSize(QtCore.QSize(540, 360))
        FirstWindow.setMaximumSize(QtCore.QSize(540, 360))
        FirstWindow.setMouseTracking(True)
        FirstWindow.setStyleSheet("*{\n"
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
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(180, 0, 181, 121))
        self.label_logo.setStyleSheet("image: url(:/images/Logo.png)")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.commandLinkButton.setMouseTracking(True)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 80, 141, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 330, 121, 41))
        self.label_2.setObjectName("label_2")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(90, 120, 361, 200))
        self.webEngineView.setStyleSheet("")
        self.webEngineView.setUrl(QtCore.QUrl("file:///ATMMap1.html"))
        self.webEngineView.setObjectName("webEngineView")
        FirstWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FirstWindow)
        self.statusbar.setObjectName("statusbar")
        FirstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FirstWindow)
        self.toolButton.clicked.connect(FirstWindow.close)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "ATM Locator"))
        self.toolButton.setText(_translate("FirstWindow", "..."))
        self.commandLinkButton.setText(_translate("FirstWindow", "Back to Main Menu"))
        self.label.setText(_translate("FirstWindow", "ATM Locator"))
        self.label_2.setText(_translate("FirstWindow", "ATM Locator"))
from PyQt5 import QtWebEngineWidgets
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    sys.exit(app.exec_())
