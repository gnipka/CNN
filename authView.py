from PyQt5 import QtWidgets
import view.auth
from dbWorker import dbWorker
import ctypes

from specialist import SpecialistApp
from user import UserApp

class AuthApp(QtWidgets.QMainWindow, view.auth.Ui_MainWindow):

    # конструктор
    def __init__(self):
        super().__init__()
        self.setupUi(self) # инициализация дизайна
        self.pbEntry.clicked.connect(self.tryAuth)
        self.db = dbWorker()
        #self.lbLogin.setText('specialist')
        #self.lbPass.setText('specialist')

    # авторизация
    def tryAuth(self):
        role = self.db.isAuthorized(self.lbLogin.text(), self.lbPass.text())
        print(role)
        if role is None:
            ctypes.windll.user32.MessageBoxW(0, "Доступ запрещен", "Авторизация", 0)
        elif role[0] == 'engineer':
            self.hide()
            self.dialog = UserApp()
            self.dialog.show()
        elif role[0] == 'specialist':
            self.hide()
            self.dialog = SpecialistApp()
            self.dialog.show()
        else:
            ctypes.windll.user32.MessageBoxW(0, "Доступ запрещен", "Авторизация", 0)