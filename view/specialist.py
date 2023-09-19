# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gnipk\Downloads\Telegram Desktop\UI\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 816)
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
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 721, 111))
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
        self.CountHiddenLayer = QtWidgets.QComboBox(self.groupBox)
        self.CountHiddenLayer.setGeometry(QtCore.QRect(180, 40, 71, 22))
        self.CountHiddenLayer.setObjectName("CountHiddenLayer")
        self.levels = QtWidgets.QLabel(self.groupBox)
        self.levels.setGeometry(QtCore.QRect(10, 30, 161, 36))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.levels.setFont(font)
        self.levels.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.levels.setObjectName("levels")
        self.levels_2 = QtWidgets.QLabel(self.groupBox)
        self.levels_2.setGeometry(QtCore.QRect(270, 30, 91, 36))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.levels_2.setFont(font)
        self.levels_2.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.levels_2.setObjectName("levels_2")
        self.Size = QtWidgets.QComboBox(self.groupBox)
        self.Size.setGeometry(QtCore.QRect(370, 40, 71, 22))
        self.Size.setObjectName("Size")
        self.levels_3 = QtWidgets.QLabel(self.groupBox)
        self.levels_3.setGeometry(QtCore.QRect(460, 30, 171, 36))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.levels_3.setFont(font)
        self.levels_3.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.levels_3.setObjectName("levels_3")
        self.MaxEpochs = QtWidgets.QComboBox(self.groupBox)
        self.MaxEpochs.setGeometry(QtCore.QRect(630, 40, 71, 22))
        self.MaxEpochs.setObjectName("MaxEpochs")
        self.levels_6 = QtWidgets.QLabel(self.groupBox)
        self.levels_6.setGeometry(QtCore.QRect(25, 75, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.levels_6.setFont(font)
        self.levels_6.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.levels_6.setObjectName("levels_6")
        self.NameModel = QtWidgets.QLineEdit(self.groupBox)
        self.NameModel.setGeometry(QtCore.QRect(180, 75, 191, 22))
        self.NameModel.setText("")
        self.NameModel.setObjectName("NameModel")
        # self.levels_5 = QtWidgets.QLabel(self.groupBox)
        # self.levels_5.setGeometry(QtCore.QRect(10, 70, 91, 36))
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei UI Light")
        # font.setPointSize(10)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(50)
        # self.levels_5.setFont(font)
        # self.levels_5.setStyleSheet("border: none;\n"
        #                             "font: 10pt \"Microsoft YaHei UI Light\";\n"
        #                             "")
        # self.levels_5.setObjectName("levels_5")
        # self.Error = QtWidgets.QDoubleSpinBox(self.groupBox)
        # self.Error.setGeometry(QtCore.QRect(100, 80, 62, 22))
        # self.Error.setObjectName("Error")
        self.pbTable = QtWidgets.QPushButton(self.groupBox)
        self.pbTable.setGeometry(QtCore.QRect(390, 75, 161, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbTable.setFont(font)
        self.pbTable.setStyleSheet("background-color: rgb(164, 166, 165);\n"
                                   "border: 2px solid rgb(164, 166, 165);\n"
                                   "border-radius: 5px;")
        self.pbTable.setObjectName("pbTable")
        self.pbTrain = QtWidgets.QPushButton(self.centralwidget)
        self.pbTrain.setGeometry(QtCore.QRect(20, 480, 721, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbTrain.setFont(font)
        self.pbTrain.setStyleSheet("background-color: rgb(164, 166, 165);\n"
"border: 2px solid rgb(164, 166, 165);\n"
"border-radius: 5px;")
        self.pbTrain.setObjectName("pbTrain")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 570, 721, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("border: 1px solid rgb(164, 166, 165);\n"
"border-radius: 1px;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"background-color: rgb(255, 255, 255);\n"
"QGroupBox > QLabell{\n"
"    border:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 30, 481, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mse = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        # self.mse.setFont(font)
        # self.mse.setStyleSheet("border: none;")
        # self.mse.setObjectName("mse")
        # self.gridLayout.addWidget(self.mse, 0, 1, 1, 1)
        self.mae = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mae.setFont(font)
        self.mae.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.mae.setObjectName("mae")
        self.gridLayout.addWidget(self.mae, 0, 0, 1, 1)
        # self.mape = QtWidgets.QLabel(self.gridLayoutWidget)
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei UI Light")
        # font.setPointSize(10)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(50)
        # self.mape.setFont(font)
        # self.mape.setStyleSheet("border-color: rgb(255, 255, 255);")
        # self.mape.setObjectName("mape")
        # self.gridLayout.addWidget(self.mape, 0, 2, 1, 1)
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
        self.gridLayout.addWidget(self.recall, 1, 0, 1, 1)
        self.precision = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.precision.setFont(font)
        self.precision.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.precision.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.precision.setObjectName("precision")
        self.gridLayout.addWidget(self.precision, 1, 1, 1, 1)
        self.F1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.F1.setFont(font)
        self.F1.setStyleSheet("border-color: rgb(255, 255, 255);")
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
        self.pbChart.setGeometry(QtCore.QRect(20, 710, 341, 35))
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
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 520, 721, 41))
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
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 180, 721, 201))
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
        self.PredictQuality = QtWidgets.QComboBox(self.groupBox_4)
        self.PredictQuality.setGeometry(QtCore.QRect(270, 40, 431, 22))
        self.PredictQuality.setObjectName("PredictQuality")
        self.levels_4 = QtWidgets.QLabel(self.groupBox_4)
        self.levels_4.setGeometry(QtCore.QRect(10, 30, 241, 36))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.levels_4.setFont(font)
        self.levels_4.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.levels_4.setObjectName("levels_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(70, 67, 171, 36))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;\n"
"font: 10pt \"Microsoft YaHei UI Light\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.ControlActions = QtWidgets.QListWidget(self.groupBox_4)
        self.ControlActions.setGeometry(QtCore.QRect(270, 80, 431, 111))
        self.ControlActions.setObjectName("ControlActions")
        self.pbLoss = QtWidgets.QPushButton(self.centralwidget)
        self.pbLoss.setGeometry(QtCore.QRect(370, 710, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbLoss.setFont(font)
        self.pbLoss.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "border: 2px solid rgb(164, 166, 165);\n"
                                  "border-radius: 5px;\n"
                                  "")
        self.pbLoss.setObjectName("pbLoss")
        self.pbROC = QtWidgets.QPushButton(self.centralwidget)
        self.pbROC.setGeometry(QtCore.QRect(560, 710, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbROC.setFont(font)
        self.pbROC.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(164, 166, 165);\n"
"border-radius: 5px;\n"
"")
        self.pbROC.setObjectName("pbROC")
        self.pbBack = QtWidgets.QPushButton(self.centralwidget)
        self.pbBack.setGeometry(QtCore.QRect(665, 10, 121, 35))
        self.pbBack.setIcon(QtGui.QIcon('imgs/pbBack.ico'))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbBack.setFont(font)
        self.pbBack.setStyleSheet("background-color: rgb(164, 166, 165);\n"
"border: 2px solid rgb(164, 166, 165);\n"
"border-radius: 5px;")
        self.pbBack.setText("")
        self.pbBack.setObjectName("pbBack")
        self.pbSaveModel = QtWidgets.QPushButton(self.centralwidget)
        self.pbSaveModel.setGeometry(QtCore.QRect(20, 760, 721, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbSaveModel.setFont(font)
        self.pbSaveModel.setStyleSheet("background-color: rgb(164, 166, 165);\n"
"border: 2px solid rgb(164, 166, 165);\n"
"border-radius: 5px;")
        self.pbSaveModel.setObjectName("pbSaveModel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 390, 491, 75))
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
        self.label_4.setGeometry(QtCore.QRect(20, 30, 21, 31))
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
        self.dateTimeStart.setGeometry(QtCore.QRect(40, 30, 194, 27))
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
        self.label_5.setGeometry(QtCore.QRect(250, 30, 31, 31))
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
        self.dateTimeEnd.setGeometry(QtCore.QRect(280, 30, 194, 27))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeEnd.setFont(font)
        self.dateTimeEnd.setStyleSheet("border: 1px solid rgb(164, 166, 165);")
        self.dateTimeEnd.setObjectName("dateTimeEnd")
        self.textPB = QtWidgets.QLabel(self.centralwidget)
        self.textPB.setGeometry(QtCore.QRect(30, 530, 701, 21))
        self.textPB.setAlignment(QtCore.Qt.AlignCenter)
        self.textPB.setObjectName("textPB")
        self.textPB.setStyleSheet("background: transparent;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pbLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pbLoad.setGeometry(QtCore.QRect(520, 390, 221, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbLoad.setFont(font)
        self.pbLoad.setStyleSheet("background-color: rgb(164, 166, 165);\n"
                                  "border: 2px solid rgb(164, 166, 165);\n"
                                  "border-radius: 5px;")
        self.pbLoad.setObjectName("pbLoad")
        self.pbTrend = QtWidgets.QPushButton(self.centralwidget)
        self.pbTrend.setGeometry(QtCore.QRect(520, 430, 221, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pbTrend.setFont(font)
        self.pbTrend.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border: 2px solid rgb(164, 166, 165);\n"
                                   "border-radius: 5px;\n"
                                   "")
        self.pbTrend.setObjectName("pbTrend")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Синтез модели"))
        self.label.setText(_translate("MainWindow", "Обучение модели"))
        self.groupBox.setTitle(_translate("MainWindow", "Настройки модели"))
        self.levels.setText(_translate("MainWindow", "Количество скрытых слоев"))
        self.levels_2.setText(_translate("MainWindow", "Размер пакета"))
        self.levels_3.setText(_translate("MainWindow", "Максимальное число эпох"))
        self.levels_6.setText(_translate("MainWindow", "Наименование модели"))
        self.pbTrain.setText(_translate("MainWindow", "Обучение"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Верификация модели"))
        self.mae.setText(_translate("MainWindow", "MAE = "))
        self.rmse.setText(_translate("MainWindow", " RMSE = "))
        self.recall.setText(_translate("MainWindow", " recall = "))
        self.precision.setText(_translate("MainWindow", "precision = "))
        self.F1.setText(_translate("MainWindow", "F1 = "))
        self.AUC.setText(_translate("MainWindow", " AUC = "))
        self.pbChart.setText(_translate("MainWindow", "График реальных и спрогнозированных величин"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Настройки прогнозирования"))
        self.levels_4.setText(_translate("MainWindow", "Прогнозируемый показатель качества"))
        self.label_3.setText(_translate("MainWindow", "Управляющие воздействия"))
        self.pbROC.setText(_translate("MainWindow", "ROC-кривая"))
        self.pbSaveModel.setText(_translate("MainWindow", "Сохранить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Выбор временного диапазона"))
        self.label_4.setText(_translate("MainWindow", "с"))
        self.label_5.setText(_translate("MainWindow", "по"))
        self.pbLoad.setText(_translate("MainWindow", "Загрузить данные"))
        self.pbTrend.setText(_translate("MainWindow", "Построить тренды"))
        self.pbLoss.setText(_translate("MainWindow", "График обучения модели"))
        # self.levels_5.setText(_translate("MainWindow", "Погрешность"))
        self.pbTable.setText(_translate("MainWindow", "Таблица моделей"))