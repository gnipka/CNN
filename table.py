from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtWidgets import QHeaderView
import ctypes

import view.table
from dbWorker import dbWorker
class TableApp(QtWidgets.QMainWindow, view.table.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = dbWorker()
        self.updateTable()
    def removeModel(self):
        value = self.tableWidget.currentIndex().row()
        result = ctypes.windll.user32.MessageBoxW(0, f"Вы действильно хотите удалить модель {self.models[self.ids[value]]['name']}?", "Удаление модели", 4)
        if(result == 6):
            self.db.removeModel(self.ids[value])
            self.updateTable()

    def updateTable(self):
        self.db.loadParameters()
        self.db.loadNameModel()
        self.models = self.db.loadModels()
        self.ids = dict()
        self.tableWidget.setRowCount(len(self.models))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Наименование модели", "Начальная дата", "Конечная дата", "Количество скрытых слоев",
             "Размер пакета данных", "Максимальное число эпох", "Удалить"])

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i, (key, value) in enumerate(self.models.items()):
            self.coefficients = self.db.loadCoefficient(value['name'])
            self.ids[i] = key
            self.tableWidget.verticalHeaderVisible = False
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(value['name']))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(value['dateStart']))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(value['dateEnd']))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.coefficients['HiddenSize'])))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.coefficients['BatchSize'])))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(self.coefficients['Epochs'])))
            icon = Qt.QIcon()
            icon.addFile('imgs/pbRemove.ico')
            item = Qt.QPushButton()
            item.setStyleSheet("border-style: none")
            item.setIcon(icon)
            item.clicked.connect(self.removeModel)
            self.tableWidget.setCellWidget(i, 6, item)

    def message(self, title, body):
            ctypes.windll.user32.MessageBoxW(0, body, title, 0)