# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'branchLocOp2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window2(object):
    def setupUi(self, Window2):
        Window2.setObjectName("Branch Locator")
        Window2.resize(540, 360)
        Window2.setMinimumSize(QtCore.QSize(540, 360))
        Window2.setMaximumSize(QtCore.QSize(540, 360))
        Window2.setStyleSheet("*{\n"
"font-family: Akrobat;\n"
"}\n"
"QMainWindow{\n"
"border-image:url(:/images/BG.jpg)\n"
"}\n"
"QCommandLinkButton{\n"
"font-family: Akrobat;\n"
"font-size: 12px;\n"
"}\n"
"QCommandLinkButton:hover{\n"
"background: #2E5984;\n"
"border-radius: 10px;\n"
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
        self.centralwidget = QtWidgets.QWidget(Window2)
        self.centralwidget.setObjectName("centralwidget")
        self.closeIcon = QtWidgets.QToolButton(self.centralwidget)
        self.closeIcon.setGeometry(QtCore.QRect(510, 10, 21, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeIcon.setIcon(icon)
        self.closeIcon.setIconSize(QtCore.QSize(50, 50))
        self.closeIcon.setObjectName("closeIcon")
        self.enterLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.enterLocation.setGeometry(QtCore.QRect(180, 310, 201, 21))
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
        self.searchIcon.setGeometry(QtCore.QRect(390, 310, 21, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/iconfinder_Search_858732.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchIcon.setIcon(icon1)
        self.searchIcon.setIconSize(QtCore.QSize(40, 40))
        self.searchIcon.setCheckable(True)
        self.searchIcon.setObjectName("searchIcon")
        self.displayText = QtWidgets.QLabel(self.centralwidget)
        self.displayText.setGeometry(QtCore.QRect(210, 70, 141, 21))
        self.displayText.setAlignment(QtCore.Qt.AlignCenter)
        self.displayText.setWordWrap(False)
        self.displayText.setIndent(0)
        self.displayText.setObjectName("displayText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, -30, 201, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../branchLocator draft/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.commandLinkButton.setMouseTracking(True)
        self.commandLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton.setAutoFillBackground(False)
        self.commandLinkButton.setStyleSheet("")
        self.commandLinkButton.setIconSize(QtCore.QSize(20, 10))
        self.commandLinkButton.setDescription("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(90, 100, 381, 200))
        self.webEngineView.setUrl(QtCore.QUrl("file:///map2.html"))
        self.webEngineView.setObjectName("webEngineView")
        self.label.raise_()
        self.closeIcon.raise_()
        self.enterLocation.raise_()
        self.searchIcon.raise_()
        self.displayText.raise_()
        self.commandLinkButton.raise_()
        self.webEngineView.raise_()
        Window2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window2)
        self.statusbar.setObjectName("statusbar")
        Window2.setStatusBar(self.statusbar)

        self.retranslateUi(Window2)
        self.closeIcon.clicked.connect(Window2.close)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        _translate = QtCore.QCoreApplication.translate
        Window2.setWindowTitle(_translate("Window2", "Branch Locator"))
        self.closeIcon.setText(_translate("Window2", "..."))
        self.enterLocation.setPlaceholderText(_translate("Window2", "               Enter your location"))
        self.searchIcon.setText(_translate("Window2", "..."))
        self.displayText.setText(_translate("Window2", "Branch Locator"))
        self.commandLinkButton.setText(_translate("Window2", "Back to Main Menu"))
from PyQt5 import QtWebEngineWidgets
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window2 = QtWidgets.QMainWindow()
    ui = Ui_Window2()
    ui.setupUi(Window2)
    Window2.show()
    sys.exit(app.exec_())
