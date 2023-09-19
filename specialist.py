from PyQt5 import QtWidgets, QtCore
import threading
import numpy as np
import time
import matplotlib
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import ctypes
from datetime import datetime
import pandas as pd

import view.specialist
import authView
import table
from dbWorker import dbWorker
from model import model
from metrics import metrics
from plotlyView import PlotlyViewer
from statsmodels.tsa.seasonal import seasonal_decompose
HIDDENSIZE = [1, 2, 3, 4, 5]
BATCHSIZE = [2, 4, 8, 16, 32, 64, 128, 256]
TRAINEPOCHS = [1, 10, 50, 100, 500, 1000]

class SpecialistApp(QtWidgets.QMainWindow, view.specialist.Ui_MainWindow):

    # конструтор
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbBack.clicked.connect(self.goToAuth)
        self.pbTrain.clicked.connect(self.education)
        self.pbChart.clicked.connect(self.chart)
        self.pbROC.clicked.connect(self.drawROC)
        self.db = dbWorker()
        self.loadParameter()
        self.setDate()
        self.pbSaveModel.clicked.connect(self.save)
        self.pbTrend.clicked.connect(self.drawTrend)
        self.pbLoad.clicked.connect(self.loadData)
        self.pbLoss.clicked.connect(self.drawLoss)
        self.pbTable.clicked.connect(self.goToTable)
        self.frame = pd.DataFrame()

    def loadParameter(self):

        self.db.loadParameters()
        x = self.db.x
        y = self.db.y
        value = x[1]
        defects = self.db.defects
        ruNames = self.db.ruNames

        for key in defects.keys():
            if(ruNames[key] != 'nan'):
                self.PredictQuality.addItem(ruNames[key], key)

        for value in HIDDENSIZE:
            self.CountHiddenLayer.addItem(str(value))

        for value in BATCHSIZE:
            self.Size.addItem(str(value))

        for value in TRAINEPOCHS:
            self.MaxEpochs.addItem(str(value))

        features = self.db.features
        self.MyRole = QtCore.Qt.UserRole + 2
        for key in features.keys():
            item = QtWidgets.QListWidgetItem()
            item.setText(ruNames[key])
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setData(self.MyRole, key)
            self.ControlActions.addItem(item)

    # прогресс бар
    def thread(my_func):
        def wrapper(*args, **kwargs):
            my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
            my_thread.start()

        return wrapper

    @thread
    def education(self, true):

        if (len(self.frame) == 0):
            self.message('Ошибка при обучении модели', 'Перед обучением модели необходимо загрузить данные')

        elif (len(self.NameModel.text()) == 0):
            self.message('Ошибка при обучении модели', 'Перед обучением модели необходимо ввести наименование модели')

        else:
            self.textPB.setText('Обучение модели...')
            self.progressBar.setMaximum(0)
            self.currentModel = model(self.NameModel.text(), 0)
            self.coefficients = {"HiddenSize": self.CountHiddenLayer.currentText(), "BatchSize": self.Size.currentText(), "Epochs": self.MaxEpochs.currentText()}
            trues, preds, self.dates, self.loss = self.currentModel.education(self.coefficients, self.frame)

            self.pred_scales = []
            self.true_scales = []
            for item in preds:
                self.pred_scales.append(np.mean(item))
            for item in trues:
                self.true_scales.append(np.mean(item))

            for i in range(len(self.true_scales)):
                if self.true_scales[i] < 0:
                    self.true_scales[i] = 0

            for i in range(len(self.pred_scales)):
                if self.pred_scales[i] < 0:
                    self.pred_scales[i] = 0


            self.metric = metrics(self.true_scales, self.pred_scales, self.db.limits[self.PredictQuality.currentData()][1])
            mae = self.mae.text().split('=', 1)[0] + '= ' + str(round(self.metric.mae(), 2))
            self.mae.setText(mae)
            rmse = self.rmse.text().split('=', 1)[0] + '= ' + str(round(self.metric.rmse(), 2))
            self.rmse.setText(rmse)
            auc = self.AUC.text().split('=', 1)[0] + '= ' + str(round(self.metric.auc(), 2))
            self.AUC.setText(auc)
            precision = self.precision.text().split('=', 1)[0] + '= ' + str(round(self.metric.precision(), 2))
            self.precision.setText(precision)
            recall = self.recall.text().split('=', 1)[0] + '= ' + str(round(self.metric.recall(), 2))
            self.recall.setText(recall)
            F1 = self.F1.text().split('=', 1)[0] + '= ' + str(round(self.metric.f1(), 2))
            self.F1.setText(F1)
            self.progressBar.setMaximum(100)
            self.textPB.setText('Обучение завершено')

    @thread
    def loadData(self, true):

        self.controlActionsItems = dict()
        for i in range(self.ControlActions.count()):
            if (self.ControlActions.item(i).checkState() == QtCore.Qt.Checked):
                self.controlActionsItems[self.ControlActions.item(i).data(self.MyRole)] = self.ControlActions.item(
                    i).text()

        if (len(self.controlActionsItems) == 0):
            self.message('Ошибка при загрузке данных', 'Перед загрузкой данных выберите хотя бы одно управляющее воздействие')

        else:
            self.textPB.setText('Загрузка данных...')
            self.progressBar.setMaximum(0)
            self.frame = self.db.loadParameterValues(self.PredictQuality.currentData(), self.controlActionsItems,
                                                self.dateTimeStart.dateTime().toPyDateTime(),
                                                self.dateTimeEnd.dateTime().toPyDateTime())
            self.progressBar.setMaximum(100)
            self.textPB.setText('Данные успешно загружены')

    def drawROC(self, true):
        matplotlib.rcParams['figure.figsize'] = (5, 5)
        matplotlib.rcParams['axes.grid'] = True
        plt.plot(self.metric.FPR, self.metric.TPR, label='ROC curve ')
        plt.plot([0, 1], [0, 1])
        plt.xlim([0.0, 1.01])
        plt.ylim([0.0, 1.01])
        plt.xlabel('Доля ложных положительных решений')
        plt.ylabel('Доля верных положительных решений')
        plt.title('ROC-кривая')
        plt.show()

    def drawLoss(self):
        if(len(self.loss) == 0):
            self.message('Ошибка при построении графика обучения модели', 'Перед построением графика необходимо обучить модель')
        else:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(range(1, len(self.loss[0]))), y=self.loss[0]))
            fig.update_xaxes(title='Номер эпохи')
            fig.update_yaxes(title='Значение MSE')
            win = PlotlyViewer(fig, "График обучения модели")

    def chart(self):
        x_chart = self.dates.to_numpy()[:len(self.true_scales)]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_chart, y=self.true_scales, name='Производственные данные'))
        fig.add_trace(go.Scatter(x=x_chart, y=self.pred_scales, name='Спрогнозированные данные'))
        fig.add_trace(go.Scatter(x=x_chart, y=[self.db.limits[self.PredictQuality.currentData()][1]] * len(self.true_scales), name='Верхняя граница'))
        win = PlotlyViewer(fig, "График производственных и спрогнозированных значений")

    def drawTrend(self):

        if(len(self.frame)):
            x_chart = self.frame.index
            fig = make_subplots(rows=len(self.controlActionsItems)+1, cols=1)

            fig.add_trace(go.Scatter(x=x_chart, y=self.frame['OT'], showlegend=False), 1, 1)
            fig.update_yaxes(title=self.db.ruNames[self.PredictQuality.currentData()] + ', ' + self.db.units[self.PredictQuality.currentData()], titlefont=dict(size=10), title_standoff=10, col=1, row=1)
            fig.update_xaxes(title='Дата', titlefont=dict(size=10), title_standoff=10, col=1, row=1)

            i = 2
            for key, name in self.controlActionsItems.items():
                fig.add_trace(go.Scatter(x=x_chart, y=self.frame[self.db.parameters[key]], showlegend=False, name=self.db.ruNames[key] + ', ' + self.db.units[key]), i, 1)
                fig.update_xaxes(title='Дата', titlefont=dict(size=14), title_standoff=10, col=1, row=i)
                fig.update_yaxes(title=self.db.ruNames[key] + ', ' + self.db.units[key], titlefont=dict(size=10), title_standoff=10, col=1, row=i)
                i += 1
            win = PlotlyViewer(fig, "Тренды параметров")
        else:
            self.message('Ошибка при построении графика трендов параметров', 'Перед построением графика необходимо загрузить данные')


    def save(self):

        items = dict()

        for i in range(self.ControlActions.count() - 1):
            if(self.ControlActions.item(i).checkState() == QtCore.Qt.Checked):
                items[self.ControlActions.item(i).data(self.MyRole)] = self.ControlActions.item(i).text()
        self.db.saveModel(self.currentModel.name, self.dateTimeStart.dateTime().toString('yyyy-MM-dd hh:mm:ss'), self.dateTimeEnd.dateTime().toString('yyyy-MM-dd hh:mm:ss'), self.coefficients, self.PredictQuality.currentData(), items)
        ctypes.windll.user32.MessageBoxW(0, f'Модель {self.currentModel.name} сохранена', "Обучение модели", 0)
    def setDate(self):
        # отображение календаря
        self.dateTimeStart.setCalendarPopup(True)
        self.dateTimeEnd.setCalendarPopup(True)
        # установка мин и макс даты
        self.dateTimeStart.setMinimumDateTime(datetime.strptime(self.db.minDate, '%Y-%m-%d %H:%M:%S'))
        self.dateTimeEnd.setMinimumDateTime(datetime.strptime(self.db.minDate, '%Y-%m-%d %H:%M:%S'))
        self.dateTimeStart.setMaximumDateTime(datetime.strptime(self.db.maxDate, '%Y-%m-%d %H:%M:%S'))
        self.dateTimeEnd.setMaximumDateTime(datetime.strptime(self.db.maxDate, '%Y-%m-%d %H:%M:%S'))
        # запись даты в лейбл
        self.dateTimeStart.setDateTime(datetime.strptime(self.db.minDate, '%Y-%m-%d %H:%M:%S'))
        self.dateTimeEnd.setDate(datetime.strptime(self.db.maxDate, '%Y-%m-%d %H:%M:%S'))

    def goToTable(self):
        self.dialog = table.TableApp()
        self.dialog.show()

    # переход к окну авторизации
    def goToAuth(self):
        self.hide()
        self.dialog = authView.AuthApp()
        self.dialog.show()

    def message(self, title, body):
            ctypes.windll.user32.MessageBoxW(0, body, title, 0)