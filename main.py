
from PyQt5.QtWidgets import QApplication
import PyQt5.uic as uic
import sys
from ui_list import UiList
from events.login import event

app = QApplication(sys.argv)
login_form = uic.loadUi(UiList.LOGIN)

login_event = event.Event(login_form).response

login_form.btn_login.clicked.connect(login_event)

login_form.show()
app.exec_() 