from PyQt5 import QtWidgets, QtCore
import threading
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime
import time
import plotly.graph_objs as go
import pandas as pd

import authView
from dbWorker import dbWorker
import view.user
from model import model
from metrics import metrics
from plotlyView import PlotlyViewer


class UserApp(QtWidgets.QMainWindow, view.user.Ui_MainWindow):

    # конструктор
    def __init__(self):
        super().__init__()

        self.setupUi(self) # инициализация дизайна
        self.db = dbWorker()
        self.db.loadParameters()
        self.pbPredict.clicked.connect(self.tryPredict)
        self.pbChart.clicked.connect(self.chart)
        self.ROC.clicked.connect(self.drawROC)
        self.pbBack.clicked.connect(self.goToAuth)

        self.setDate()
        self.setModels()
        self.setParam()
        self.cbModels.currentTextChanged.connect(self.setParam)

    # меню моделей
    def setModels(self):
        self.name_model = self.db.loadNameModel()

        for key, value in self.name_model.items():
            self.cbModels.addItem(value, key)
        text = self.cbModels.currentText()
        data = self.cbModels.currentData()
        self.currentModel = model(self.cbModels.currentText(), self.cbModels.currentData())

    # работа с календариками
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

    # прогресс бар
    def thread(my_func):
        def wrapper(*args, **kwargs):
            my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
            my_thread.start()

        return wrapper

    # прогнозирование
    @thread
    def tryPredict(self, true):
        self.textPB.setText('Загрузка данных...')
        self.progressBar.setMaximum(0)
        self.controlActionsItems = dict()

        for i in range(self.controlActions.count()):
            self.controlActionsItems[self.controlActions.item(i).data(self.MyRole)] = self.controlActions.item(i).text()

        self.frame = pd.DataFrame()
        self.frame = self.db.loadParameterValues(self.defectKey, self.controlActionsItems, self.dateTimeStart.dateTime().toPyDateTime(), self.dateTimeEnd.dateTime().toPyDateTime())
        self.progressBar.setMaximum(100)
        self.textPB.setText('Данные успешно загружены')
        time.sleep(2)
        self.textPB.setText('Прогнозирование...')
        self.progressBar.setMaximum(0)
        pred, true, true_scale, pred_scale, self.dates = self.currentModel.predict(self.frame, self.coefficients, self.currentModel.name)
        self.preds = pred.reshape(-1, pred.shape[-2], pred.shape[-1])
        self.trues = true.reshape(-1, true.shape[-2], true.shape[-1])
        self.pred_scale = pred_scale.reshape(-1, pred_scale.shape[-2], pred_scale.shape[-1])
        self.true_scale = true_scale.reshape(-1, true_scale.shape[-2], true_scale.shape[-1])

        self.pred_scales = []
        self.true_scales = []
        for item in self.pred_scale:
            self.pred_scales.append(item[0][0])
        for item in self.true_scale:
            self.true_scales.append(item[23][0])

        for i in range(len(self.true_scales)):
            if self.true_scales[i] < 0:
                self.true_scales[i] = 0

        for i in range(len(self.pred_scales)):
            if self.pred_scales[i] < 0:
                self.pred_scales[i] = 0

        self.metric = metrics(self.true_scales, self.pred_scales, self.db.limits[self.defectKey][1])
        # mse = self.mse.text().split('=', 1)[0] + '= ' + str(round(self.metric.mse(), 2))
        # self.mse.setText(mse)
        mae = self.mae.text().split('=', 1)[0] + '= ' + str(round(self.metric.mae(), 2))
        self.mae.setText(mae)
        # mape = self.mape.text().split('=', 1)[0] + '= ' + str(round(self.metric.mape(), 2))
        # self.mape.setText(mape)
        rmse = self.rmse.text().split('=', 1)[0] + '= ' + str(round(self.metric.rmse(), 2))
        self.rmse.setText(rmse)
        tryAUC = self.metric.auc()
        if(tryAUC != ""):
            auc = self.AUC.text().split('=', 1)[0] + '= ' + str(round(self.metric.auc(), 2))
            self.AUC.setText(auc)
        precision = self.precision.text().split('=', 1)[0] + '= ' + str(round(self.metric.precision(), 2))
        self.precision.setText(precision)
        recall = self.recall.text().split('=', 1)[0] + '= ' + str(round(self.metric.recall(), 2))
        self.recall.setText(recall)
        F1 = self.F1.text().split('=', 1)[0] + '= ' + str(round(self.metric.f1(), 2))
        self.F1.setText(F1)
        self.progressBar.setMaximum(100)

        # print(f"(TP) Не дефект распознался как не дефект: {self.metric.TP}")
        # print(f"(FN) Не дефект распознался как дефект   : {self.metric.FN}")
        # print(f"(FP) Дефект распознался как не дефект   : {self.metric.FP}")
        # print(f"(TN) Дефект распознался как дефект      : {self.metric.TN}")

        self.textPB.setText('Прогнозирование завершено')

    # график ROC-кривой
    def drawROC(self, true):
        fig, ax = plt.subplots()
        ax.plot(self.metric.FPR, self.metric.TPR, label='ROC curve')
        ax.plot([0, 1], [0, 1])
        plt.xlabel('Доля ложных положительных значений')
        plt.ylabel('Доля верных положительных значений')
        plt.title('ROC-кривая')
        plt.show()

    # загрузка параметров модели
    def setParam(self):
        self.currentModel = model(self.cbModels.currentText(), self.cbModels.currentData())
        self.coefficients = self.db.loadCoefficient(self.currentModel.name)

        batch = self.batchSize.text().split('=', 1)[0] + '= ' + str(self.coefficients['BatchSize'])
        self.batchSize.setText(batch)

        hiddenSize = self.hiddenSize.text().split('=', 1)[0] + '= ' + str(self.coefficients['HiddenSize'])
        self.hiddenSize.setText(hiddenSize)

        epochs = self.epochs.text().split('=', 1)[0] + '= ' + str(self.coefficients['Epochs'])
        self.epochs.setText(epochs)

        defect, self.defectKey = self.db.getModelPredictableDefect(self.currentModel.id)
        self.defect.setText(defect)

        self.MyRole = QtCore.Qt.UserRole + 2
        actionControls = self.db.getModelRelevantParameters(self.currentModel.id)

        for key, value in actionControls.items():
            item = QtWidgets.QListWidgetItem()
            item.setText(value)
            item.setData(self.MyRole, key)
            self.controlActions.addItem(item)


    # график спрогнозированных и реальных данных
    def chart(self):
        x_chart = self.dates.to_numpy()[:len(self.true_scales)]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_chart, y=self.true_scales, name='Производственные данные'))
        fig.add_trace(go.Scatter(x=x_chart, y=self.pred_scales, name='Спрогнозированные данные'))
        fig.add_trace(go.Scatter(x=x_chart, y=[self.db.limits[self.defectKey][1]] * len(self.true_scales), name='Верхняя граница'))
        fig.update_yaxes(title = self.db.ruNames[self.defectKey] + ', ' + self.db.units[self.defectKey], titlefont=dict(size=14), title_standoff=10)
        fig.update_xaxes(title='Дата', titlefont=dict(size=14), title_standoff=10)
        win = PlotlyViewer(fig, "График производственных и спрогнозированных значений")

    # переход к окну авторизации
    def goToAuth(self):
        self.hide()
        self.dialog = authView.AuthApp()
        self.dialog.show()