from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,350,1000,500)
    win.setWindowTitle("Fokin Works Mate!")
    label = QtWidgets.QLabel(win)
    web = QWebEngineView(win)
    web.move(250,0)
    web.resize(500,500)
    web.load(QUrl("file:///C:/LocalRepo/git/BankOmatic/Locator/map.html"))
    win.show()
    sys.exit(app.exec_())
    
window()
