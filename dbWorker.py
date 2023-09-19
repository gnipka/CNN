import numpy as np
import sqlite3

import pandas as pd

PATH = 'extcaland.db'


class dbWorker:
    isDataLoaded = False

    minDate = ''
    maxDate = ''

    dates = list()

    parameters = dict()  # [id] = [code]           для всех параметров
    features = dict()  # [id] = [code]             для управляющих воздействий
    defects = dict()  # [id] = [code]              для выходных параметров
    ruNames = dict()  # [id] = [ruName]            для всех параметров
    enNames = dict()  # [id] = [enName]            для всех параметров
    units = dict() # [id] = [unit]                 для единиц измерения

    limits = dict()  # limit[id][0(min)/1(max)]   для всех параметров

    all = dict()  # [id] = [values]          для всех параметров
    x = dict()  # [id] = [values]            для управляющих воздействий
    y = dict()  # [id] = [values]            для выходных параметров
    frame = dict()
    datetime = dict()
    allWithDates = dict()
    coefficients = dict() # коэффициенты модели
    models = dict() # модели

    def __init__(self):
        self.getMinMaxDates()

    # получение мин и макс дат данных
    def getMinMaxDates(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f" SELECT MIN(DateTime)"
                       f" FROM ParameterValues"
                       f" WHERE LENGTH(DateTime) = LENGTH('yyyy-mm-dd hh:mm:ss')")
        minDate = cursor.fetchall()
        cursor.execute(f" SELECT MAX(DateTime)"
                       f" FROM ParameterValues"
                       f" WHERE LENGTH(DateTime) = LENGTH('yyyy-mm-dd hh:mm:ss')")
        maxDate = cursor.fetchall()
        self.minDate = str(minDate[0][0])
        self.maxDate = str(maxDate[0][0])
        cursor.close()
        conn.close()

    # авторизация
    def isAuthorized(self, login, password):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f" SELECT Login FROM Users WHERE Login = '{login}' AND Password = '{password}'")
        login = cursor.fetchone()
        if login is not None:
            cursor.close()
            conn.close()
            return login
        cursor.close()
        conn.close()

    # загрузка параметров
    def loadParameters(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute( f" SELECT IdParameter, ParameterCode, ParameterNameRu, ParameterNameEng, IdUnit"
                        f" FROM Parameters"
                        f" WHERE IdParameterType == 2"
                        f" OR IdParameterType == 3" )
        params_row = cursor.fetchall()
        cursor.execute( f" SELECT Limits.IdParameter, LowLimitValue, HighLimitValue"
                        f" FROM Limits"
                        f" LEFT JOIN Parameters ON Parameters.IdParameter = Limits.IdParameter"
                        f" WHERE IdParameterType == 2"
                        f" OR IdParameterType == 3" )
        limits_row = cursor.fetchall()
        cursor.execute( f" SELECT Units.IdUnit, Units.Sign"
                        f" FROM Units")
        units_row = cursor.fetchall()
        units = dict()
        for item in units_row:
            units[item[0]] = item[1]

        self.allWithDates['dt'] = list()
        for row_id in range(len(params_row)):
            self.ruNames[params_row[row_id][0]] = params_row[row_id][2]
            self.enNames[params_row[row_id][0]] = params_row[row_id][3]
            self.units[params_row[row_id][0]] = units[params_row[row_id][4]]
            min = float('nan') if limits_row[row_id][1] is None else float(limits_row[row_id][1])
            max = float('nan') if limits_row[row_id][2] is None else float(limits_row[row_id][2])
            self.limits[limits_row[row_id][0]] = [min, max]
            self.parameters[params_row[row_id][0]] = params_row[row_id][1]
            if params_row[row_id][1].split('.')[0] == 'Defects':
                self.defects[params_row[row_id][0]] = params_row[row_id][1]
                self.y[params_row[row_id][0]] = list()
            else:
                self.features[params_row[row_id][0]] = params_row[row_id][1]
                self.x[params_row[row_id][0]] = list()
            self.all[params_row[row_id][0]] = list()
            self.allWithDates[params_row[row_id][0]] = list()
        cursor.close()
        conn.close()

    # наименование параметра
    def getParameterName(self, dict, id):
        return dict[id]

    # загрузка моделей
    def loadNameModel(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT *"
                       f"FROM SCIModels")
        params_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            self.models[params_row[row_id][0]] = params_row[row_id][1]
        cursor.close()
        conn.close()
        return self.models

    def loadModels(self):
        self.modelsItems = dict()
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT *"
                       f"FROM SCIModels")
        params_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            model = dict()
            model['id'] = params_row[row_id][0]
            model['name'] = params_row[row_id][1]
            model['dateStart'] = params_row[row_id][2]
            model['dateEnd'] = params_row[row_id][3]
            self.modelsItems[params_row[row_id][0]] = model
            # self.modelsItems[params_row[row_id][0]]['id'] = params_row[row_id][0]
            # self.modelsItems[params_row[row_id][0]]['name'] = params_row[row_id][1]
            # self.modelsItems[params_row[row_id][0]]['dateStart'] = params_row[row_id][2]
            # self.modelsItems[params_row[row_id][0]]['dateEnd'] = params_row[row_id][3]
        cursor.close()
        conn.close()
        return self.modelsItems

    # коэффициенты модели
    def loadCoefficient(self, name):

        currentKey = 1
        for key, value in self.models.items():
            if (value == name):
                currentKey = key

        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT SCICoefficientTypes.Name, SCICoefficients.Value "
                       f"FROM SCICoefficients "
                       f"JOIN SCIModelCoefficients "
                       f"ON SCICoefficients.IdCoefficient = SCIModelCoefficients.IdCoefficient "
                       f"JOIN SCICoefficientTypes "
                       f"ON SCICoefficients.IdCoefficientType = SCICoefficientTypes.IdCoefficientType "
                       f"WHERE IdModel == '{currentKey}'")

        params_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            self.coefficients[params_row[row_id][0]] = params_row[row_id][1]

        return self.coefficients

    # прогнозируемый дефект текущей модели
    def getModelPredictableDefect(self, key):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f" SELECT IdParameter"
                       f" FROM SCIModelParameters"
                       f" WHERE IdModelParameterType == 1"
                       f" AND IdModel == {key}")
        params_row = cursor.fetchone()
        cursor.close()
        conn.close()
        return self.getParameterName(self.ruNames, params_row[0]), params_row[0]

    # управляющие воздействия текущей модели
    def getModelRelevantParameters(self, key):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f" SELECT IdParameter"
                       f" FROM SCIModelParameters"
                       f" WHERE IdModelParameterType == 2"
                       f" AND IdModel == {key}")
        params_row = cursor.fetchall()
        result = dict()
        for row_id in range(len(params_row)):
            result[params_row[row_id][0]] = self.getParameterName(self.ruNames, params_row[row_id][0])
            # result.append(self.getParameterName(self.ruNames, params_row[row_id][0]))
        cursor.close()
        conn.close()
        return result

    def saveModel(self, nameModel, dateTimeStart, dateTimeEnd, coefficients, defect, features):

        # сохранение модели
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        query = (f" INSERT INTO SCIModels"
                 f" (Name, FromDateTime, ToDateTime)"
                 f" VALUES (?, ?, ?)")
        data = (nameModel, dateTimeStart, dateTimeEnd)
        cursor.execute(query, data)
        id = cursor.lastrowid
        conn.commit()
        cursor.close()

        # сохранение коэффициентов
        cursor = conn.cursor()
        query = (f" INSERT INTO SCICoefficients"
                 f" (Value, IdCoefficientType)"
                 f" VALUES (?, ?)")
        data = (coefficients['HiddenSize'], 1)
        cursor.execute(query, data)
        idHiddenSize = cursor.lastrowid
        conn.commit()
        data = (coefficients['BatchSize'], 2)
        cursor.execute(query, data)
        idBatchSize = cursor.lastrowid
        conn.commit()
        data = (coefficients['Epochs'], 3)
        cursor.execute(query, data)
        idEpochs = cursor.lastrowid
        conn.commit()

        # сохранение коэффициентов модели
        cursor = conn.cursor()
        query = (f" INSERT INTO SCIModelCoefficients"
                 f" (IdModel, IdCoefficient)"
                 f" VALUES (?, ?)")
        data = (id, idHiddenSize)
        cursor.execute(query, data)
        conn.commit()
        data = (id, idBatchSize)
        cursor.execute(query, data)
        conn.commit()
        data = (id, idEpochs)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()

        # сохранение параметров модели
        cursor = conn.cursor()
        query = (f" INSERT INTO SCIModelParameters"
                 f" (IdModel, IdParameter, IdModelParameterType)"
                 f" VALUES (?, ?, ?)")
        data = (id, defect, 1)
        cursor.execute(query, data)
        conn.commit()

        for value, key in features.items():
            data = (id, value, 2)
            cursor.execute(query, data)
            conn.commit()
        cursor.close()
        conn.close()

    def removeModel(self, id):

        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()

        cursor.execute(f"SELECT IdCoefficient FROM SCIModelCoefficients"
                       f" WHERE IdModel == {id}")
        idsCoef = cursor.fetchall()
        conn.commit()
        # удаление коэффициентов модели
        cursor.execute(f"DELETE FROM SCIModelCoefficients"
                       f" WHERE IdModel == {id}")
        # удаление коэффициентов
        for value in idsCoef:
            cursor.execute(f"DELETE FROM SCICoefficients"
                           f" WHERE IdCoefficient == {value[0]}")

        conn.commit()

        # удаление параметров модели
        cursor.execute(f"DELETE FROM SCIModelParameters"
                       f" WHERE IdModel = {id}")
        conn.commit()

        # удаление модели
        cursor.execute(f"DELETE FROM SCIModels"
                       f" WHERE IdModel = {id}")
        conn.commit()

        cursor.close()
        conn.close()

    def loadParameterValues(self, x, y, minDate, maxDate):
        self.frame = dict()
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f" SELECT DateTime, Value"
                       f" FROM ParameterValues"
                       f" WHERE IdParameter == {x}"
                       f" AND DateTime > '{minDate}'"
                       f" AND DateTime < '{maxDate}'")

        flag = True
        params_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            for key, name in y.items():
                cursor.execute(f" SELECT Value"
                               f" FROM ParameterValues"
                               f" WHERE IdParameter == {key}"
                               f" AND DateTime == '{params_row[row_id][0]}'")
                value = cursor.fetchone()
                if value is not None:
                    flag = True
                    self.frame.setdefault(self.parameters[key], []).append(value[0])
                else:
                    flag = False
            if flag:
                if (float(params_row[row_id][1]) > 200) :
                  self.frame.setdefault('OT', []).append(200)
                  self.frame.setdefault('date', []).append(params_row[row_id][0])
                else:
                    self.frame.setdefault('OT', []).append(params_row[row_id][1])
                    self.frame.setdefault('date', []).append(params_row[row_id][0])

        # frame = dict()
        # frame['datetime'] = self.frame.keys()
        # frame['OT'] = self.frame.values()
        # self.frame['OT'] = cursor.fetchall()

        # cursor.execute(f" SELECT DateTime"
        #                f" FROM ParameterValues"
        #                f" WHERE DateTime > '{minDate}'"
        #                f" AND DateTime < '{maxDate}'")
        # self.datetime['time'] = cursor.fetchall()

        # for key, value in y.items():
        #     cursor.execute(f" SELECT Datetime, Value"
        #                    f" FROM ParameterValues"
        #                    f" WHERE IdParameter == {key}"
        #                    f" AND DateTime > '{minDate}'"
        #                    f" AND DateTime < '{maxDate}'")
        #     params_row = cursor.fetchall()
        #     for row_id in range(len(params_row)):
        #         if params_row[row_id][0] in frame['datetime']:
        #             frame.setdefault(value, []).append(params_row[row_id][1])
        #             # values = list(frame[value].)
        #             # values.append(params_row[row_id][1])
        #             # frame[value] = values



        cursor.close()
        conn.close()

        framePD = pd.DataFrame(self.frame, dtype=np.float32)
        framePD = framePD.drop('date', axis=1)
        framePD.index = self.frame['date']
        framePD.index.name = 'date'
        print(framePD.columns)
        return framePD