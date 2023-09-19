import ctypes  # messagebox
import threading
from datetime import datetime
import matplotlib
import matplotlib.dates as mdates
import os, sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWebEngineWidgets
from matplotlib import pyplot as plt
import numpy as np
import time
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots

import view.auth
import view.specialist
import view.user
import view.admin
from authView import AuthApp
from dbWorker import dbWorker
from metrics import metrics
from model import model

HIDDENSIZE = [1, 2, 3, 4, 5]
BATCHSIZE = [2, 4, 8, 16, 32, 64, 128, 256]
TRAINEPOCHS = [1, 10, 50, 100, 500, 1000]


class AdminApp(QtWidgets.QMainWindow, view.admin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = dbWorker()
        self.db.loadParameters()
        self.parameters = self.db.parameters
        self.ruNames = self.db.ruNames
        self.enNames = self.db.enNames
        self.limits = self.db.limits
        self.tableWidget.setRowCount(len(self.parameters))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Код параметра", "Имя параметра на русском", "Имя параметра на английском", "Нижнее регламентное значение", "Верхнее регламентное значение"])
        for i, (key, value) in enumerate(self.parameters.items()):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(value))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.ruNames[key]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(self.enNames[key]))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.limits[key][0])))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.limits[key][1])))
        self.pbBack.clicked.connect(self.message)


    def message(self):
            ctypes.windll.user32.MessageBoxW(0, "Запись успешно добавлена", "Редактирование БД", 0)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AuthApp()  # Создаём объект класса AuthApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
