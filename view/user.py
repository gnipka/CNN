# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gnipk\Downloads\Telegram Desktop\UI2\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 823)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"Microsoft YaHei UI Light\";\n"
"background-color: rgb(164, 166, 165);\n"
"margin: 0 0 0 20;")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 721, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setStyleSheet("border: 1px solid rgb(164, 166, 165);\n"
"border-radius: 1px;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 35, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;")
        self.label_2.setObjectName("label_2")
        self.cbModels = QtWidgets.QComboBox(self.groupBox)
        self.cbModels.setGeometry(QtCore.QRect(150, 40, 551, 27))
        self.cbModels.setStyleSheet("border: 1px solid rgb(164, 166, 165);")
        self.cbModels.setObjectName("cbModels")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 360, 721, 81))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("border: 1px solid rgb(164, 166, 165);\n"
"border-radius: 1px;\n"
"font: 10pt \"Microsoft YaHei UI Light\";")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(140, 35, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: none;")
        self.label_4.setObjectName("label_4")
        self.dateTimeStart = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeStart.setGeometry(QtCore.QRect(170, 40, 194, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeStart.setFont(font)
        self.dateTimeStart.setStyleSheet("border: 1px solid rgb(164, 166, 165);")
        self.dateTimeStart.setObjectName("dateTimeStart")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(380, 35, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;")
        self.label_5.setObjectName("label_5")
        self.dateTimeEnd = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEnd.setGeometry(QtCore.QRect(440, 40, 194, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeEnd.setFont(font)
        self.dateTimeEnd.setStyleSheet("border: 1px solid rgb(164, 166, 165);")
        self.dateTimeEnd.setObjectName("dateTimeEnd")
        self.pbPredict = QtWidgets.QPushButton(self.centralwidget)
        self.pbPredict.setGeometry(QtCore.QRect(20, 460, 721, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbPredict.setFont(font)
        self.pbPredict.setStyleSheet("background-color: rgb(164, 166, 165);\n"
"border: 2px solid rgb(164, 166, 165);\n"
"border-radius: 5px;")
        self.pbPredict.setObjectName("pbPredict")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 580, 721, 171))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("border: 1px solid rgb(164, 166, 165);\n"
"border-radius: 1px;\n"
"font: 10pt \"Microsoft YaHei UI Light\";")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 40, 481, 115))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rmse = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rmse.setFont(font)
        self.rmse.setStyleSheet("border: none;")
        self.rmse.setObjectName("rmse")
        self.gridLayout.addWidget(self.rmse, 0, 1, 1, 1)
        self.mae = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mae.setFont(font)
        self.mae.setStyleSheet("border: none;")
        self.mae.setObjectName("mae")
        self.gridLayout.addWidget(self.mae, 0, 0, 1, 1)
        # self.mse = QtWidgets.QLabel(self.gridLayoutWidget)
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei UI Light")
        # font.setPointSize(10)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(50)
        # self.mse.setFont(font)
        # self.mse.setStyleSheet("border: none;")
        # self.mse.setObjectName("mse")
        # self.gridLayout.addWidget(self.mse, 0, 1, 1, 1)
        self.precision = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.precision.setFont(font)
        self.precision.setStyleSheet("border: none;")
        self.precision.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.precision.setObjectName("precision")
        self.gridLayout.addWidget(self.precision, 1, 0, 1, 1)
        # self.mape = QtWidgets.QLabel(self.gridLayoutWidget)
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei UI Light")
        # font.setPointSize(10)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(50)
        # self.mape.setFont(font)
        # self.mape.setStyleSheet("border: none;")
        # self.mape.setObjectName("mape")
        # self.gridLayout.addWidget(self.mape, 1, 0, 1, 1)
        self.recall = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.recall.setFont(font)
        self.recall.setStyleSheet("border: none;")
        self.recall.setObjectName("recall")
        self.gridLayout.addWidget(self.recall, 1, 1, 1, 1)
        self.F1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.F1.setFont(font)
        self.F1.setStyleSheet("border: none;")
        self.F1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.F1.setObjectName("F1")
        self.gridLayout.addWidget(self.F1, 2, 0, 1, 1)
        self.AUC = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AUC.setFont(font)
        self.AUC.setStyleSheet("border: none;")
        self.AUC.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AUC.setObjectName("AUC")
        self.gridLayout.addWidget(self.AUC, 2, 1, 1, 1)
        self.pbChart = QtWidgets.QPushButton(self.centralwidget)
        self.pbChart.setGeometry(QtCore.QRect(20, 770, 351, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbChart.setFont(font)
        self.pbChart.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(164, 166, 165);\n"
"border-radius: 5px;\n"
"")
        self.pbChart.setObjectName("pbChart")
        self.ROC = QtWidgets.QPushButton(self.centralwidget)
        self.ROC.setGeometry(QtCore.QRect(390, 770, 351, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ROC.setFont(font)
        self.ROC.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(164, 166, 165);\n"
"border-radius: 5px;\n"
"")
        self.ROC.setObjectName("ROC")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 510, 721, 41))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(142, 212, 51);\n"
"    transparent: 50;\n"
"}\n"
"QProgressBar{\n"
"    border: 2px solid rgb(164, 166, 165);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 160, 721, 191))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setTabletTracking(False)
        self.groupBox_4.setStyleSheet("border: 1px solid rgb(164, 166, 165);\n"
"border-radius: 1px;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.hiddenSize = QtWidgets.QLabel(self.groupBox_4)
        self.hiddenSize.setGeometry(QtCore.QRect(30, 30, 221, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hiddenSize.setFont(font)
        self.hiddenSize.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.hiddenSize.setObjectName("hiddenSize")
        self.batchSize = QtWidgets.QLabel(self.groupBox_4)
        self.batchSize.setGeometry(QtCore.QRect(260, 30, 141, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.batchSize.setFont(font)
        self.batchSize.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";")
        self.batchSize.setObjectName("batchSize")
        self.epochs = QtWidgets.QLabel(self.groupBox_4)
        self.epochs.setGeometry(QtCore.QRect(420, 30, 231, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.epochs.setFont(font)
        self.epochs.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";")
        self.epochs.setObjectName("epochs")
        self.features_3 = QtWidgets.QLabel(self.groupBox_4)
        self.features_3.setGeometry(QtCore.QRect(30, 70, 236, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.features_3.setFont(font)
        self.features_3.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";")
        self.features_3.setObjectName("features_3")
        self.defect = QtWidgets.QLabel(self.groupBox_4)
        self.defect.setGeometry(QtCore.QRect(280, 70, 411, 27))
        self.defect.setText("")
        self.defect.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.defect.setObjectName("defect")
        self.features_4 = QtWidgets.QLabel(self.groupBox_4)
        self.features_4.setGeometry(QtCore.QRect(95, 110, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.features_4.setFont(font)
        self.features_4.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";")
        self.features_4.setObjectName("features_4")
        self.controlActions = QtWidgets.QListWidget(self.groupBox_4)
        self.controlActions.setGeometry(QtCore.QRect(280, 115, 411, 61))
        self.controlActions.setObjectName("controlActions")
        # self.trend = QtWidgets.QPushButton(self.groupBox_4)
        # self.trend.setGeometry(QtCore.QRect(20, 155, 251, 21))
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei UI Light")
        # font.setPointSize(10)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(50)
        # self.trend.setFont(font)
        # self.trend.setStyleSheet("background-color: rgb(164, 166, 165);\n"
        #                          "border: 2px solid rgb(164, 166, 165);\n"
        #                          "border-radius: 5px;")
        # self.trend.setObjectName("trend")
        self.textPB = QtWidgets.QLabel(self.centralwidget)
        self.textPB.setGeometry(QtCore.QRect(26, 520, 711, 21))
        self.textPB.setAlignment(QtCore.Qt.AlignCenter)
        self.textPB.setObjectName("textPB")
        self.textPB.setStyleSheet("background: transparent;")
        self.pbBack = QtWidgets.QPushButton(self.centralwidget)
        self.pbBack.setGeometry(QtCore.QRect(665, 10, 121, 35))
        self.pbBack.setIcon(QtGui.QIcon('imgs/pbBack.ico'))
        self.pbBack.setFont(font)
        self.pbBack.setStyleSheet("background-color: rgb(164, 166, 165);\n"
                                  "border: 2px solid rgb(164, 166, 165);\n"
                                  "border-radius: 5px;")
        self.pbBack.setText("")
        self.pbBack.setObjectName("pbBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Прогнозирование данных"))
        self.label.setText(_translate("MainWindow", "Прогнозирование данных"))
        self.groupBox.setTitle(_translate("MainWindow", "Модель"))
        self.label_2.setText(_translate("MainWindow", "Выбор модели"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Выбор временного диапазона"))
        self.label_4.setText(_translate("MainWindow", "с"))
        self.label_5.setText(_translate("MainWindow", "по"))
        self.pbPredict.setText(_translate("MainWindow", "Прогнозирование"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Верификация модели"))
        self.rmse.setText(_translate("MainWindow", "RMSE = "))
        self.mae.setText(_translate("MainWindow", "MAE = "))
        # self.mse.setText(_translate("MainWindow", "MSE = "))
        self.precision.setText(_translate("MainWindow", "precision = "))
        # self.mape.setText(_translate("MainWindow", "MAPE = "))
        self.recall.setText(_translate("MainWindow", "recall = "))
        self.F1.setText(_translate("MainWindow", "F1 = "))
        self.AUC.setText(_translate("MainWindow", "AUC = "))
        self.pbChart.setText(_translate("MainWindow", "График реальных и спрогнозированных величин"))
        self.ROC.setText(_translate("MainWindow", "ROC-кривая"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Характеристики модели"))
        self.hiddenSize.setText(_translate("MainWindow", "Количество скрытых слоев = "))
        self.batchSize.setText(_translate("MainWindow", "Размер пакета = "))
        self.epochs.setText(_translate("MainWindow", "Максимальное число эпох = "))
        self.features_3.setText(_translate("MainWindow", "Прогнозируемый показатель качества"))
        self.features_4.setText(_translate("MainWindow", "Управляющие воздействия"))