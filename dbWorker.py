import sqlite3
import math

PATH = 'extcaland.db'


class dbWorker:
    isDataLoaded = False

    minDate = ''
    maxDate = ''

    dates = list()

    parameters = dict()  # [id] = [code]              для всех параметров
    features = dict()  # [id] = [code]              для управляющих воздействий
    defects = dict()  # [id] = [code]              для выходных параметров
    ruNames = dict()  # [id] = [ruName]            для всех параметров
    enNames = dict()  # [id] = [enName]            для всех параметров

    def __init__(self):
        self.getMinMaxDates()

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

    # def loadData(self, startDate, endDate):
    #     self.minDate = startDate
    #     self.maxDate = endDate
    #     self.loadRNNParameters()
    #     self.loadParameters()
    #     self.loadRNNModels()
    #     self.loadValues()
    #     self.isDataLoaded = True