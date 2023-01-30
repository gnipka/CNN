import sys  # sys нужен для передачи argv в QApplication
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from sklearn.metrics import roc_curve, auc
import threading
import auth
import user
from dbWorker import dbWorker
from dbModel import dbModel
from datetime import datetime
from model import model
from metrics import metrics

PATHMODELS = 'exp/data_checkpoints'

from PyQt5.QtCore import QThread, pyqtSignal

#class External(QThread):
 #   flagChanged = pyqtSignal(bool)
  #  def run(self):
   #     flag = True
    #    while (flag):
     #       self.flagChanged.emit(flag)

class UserApp(QtWidgets.QMainWindow, user.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self) # инициализация дизайна
        self.pbPredict.clicked.connect(self.try_predict)
        self.pbChart.clicked.connect(self.chart)
        self.ROC.clicked.connect(self.drawROC)

        self.db = dbWorker()
        self.dbM = dbModel()

        self.set_date()
        self.set_models()
        self.set_param()
        self.cbModels.currentTextChanged.connect(self.set_param)


    # меню моделей
    def set_models(self):
        self.name_model = self.dbM.load_name_model()
        self.cbModels.addItems(self.name_model.values())
        self.currentModel = model(self.cbModels.currentText())

    # работа с календариками
    def set_date(self):
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

    def thread(my_func):
        def wrapper(*args, **kwargs):
            my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
            my_thread.start()

        return wrapper

    @thread
    def try_predict(self, true):
        self.progressBar.setMaximum(0)

        pred, true, pred_scale, true_scale, self.dates = self.currentModel.predict(self.dateTimeStart.dateTime().toPyDateTime(), self.dateTimeEnd.dateTime().toPyDateTime())
        self.preds = []
        self.trues = []
        self.pred_scales = []
        self.true_scales = []

        for item in pred:
            self.preds.append(item.max())
        for item in true:
            self.trues.append(item.max())
        for item in pred_scale:
            self.pred_scales.append(item.max())
        for item in true_scale:
            self.true_scales.append(item.max())

        for i in range(len(self.true_scales)):
            if self.true_scales[i] < 0:
                self.true_scales[i] = 0

        self.metric = metrics(self.true_scales, self.pred_scales)
        mse = self.mse.text().split('=', 1)[0] + '= ' + str(round(self.metric.mse(), 2))
        self.mse.setText(mse)
        mae = self.mae.text().split('=', 1)[0] + '= ' + str(round(self.metric.mae(), 2))
        self.mae.setText(mae)
        mape = self.mape.text().split('=', 1)[0] + '= ' + str(round(self.metric.mape(), 2))
        self.mape.setText(mape)
        rmse = self.mape.text().split('=', 1)[0] + '= ' + str(round(self.metric.rmse(), 2))
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

    def set_param(self):
        self.lr, self.stack, self.feautur, self.batch, self.level, self.dp = self.currentModel.get_param()
        lr = self.learningRate.text().split('=', 1)[0] + '= ' + self.lr
        self.learningRate.setText(lr)

        stack = self.stacks.text().split('=', 1)[0] + '= ' + self.stack
        self.stacks.setText(stack)

        feautur = self.features.text().split('=', 1)[0] + '= ' + self.feautur
        self.features.setText(feautur)

        batch = self.batchSize.text().split('=', 1)[0] + '= ' + self.batch
        self.batchSize.setText(batch)

        level = self.levels.text().split('=', 1)[0] + '= ' + self.level
        self.levels.setText(level)

        #dp = self.dropout.text() + self.dp
        #self.dropout.setText(dp)

    def chart(self, tre):
        x_chart = self.dates.to_numpy()[:len(self.true_scales)]
        fig, ax = plt.subplots()
        y_chart1 = self.true_scales
        ax.plot(x_chart, y_chart1, color='blue', label='Производственные данные')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
        y_chart2 = self.pred_scales
        ax.plot(x_chart, y_chart2, color='magenta', label='Спрогнозированные данные')
        fig.legend()
        fig.show()

class AuthApp(QtWidgets.QMainWindow, auth.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # инициализация дизайна
        self.pbEntry.clicked.connect(self.try_auth)

    def try_auth(self):
        # dialog = UserApp(self)
        # dialog.show()
        if self.lbLogin.text() == 'admin' and self.lbPass.text() == 'admin':
            print('admin')
        elif self.lbLogin.text() == 'user' and self.lbPass.text() == 'user':
            print('user')
            self.hide()
            self.dialog = UserApp()
            self.dialog.show()
        else:
            print('error')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AuthApp()  # Создаём объект класса AuthApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
