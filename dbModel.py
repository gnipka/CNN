import sqlite3
import math

PATH = 'models.db'

class dbModel:

    def __init__(self):
        self.models = dict()
        self.coefficients = dict()

    def load_name_model(self):
        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT *"
                       f"FROM Model")
        params_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            self.models[params_row[row_id][0]] = params_row[row_id][1]
        cursor.close()
        conn.close()
        return self.models

    def load_coefficient(self, name):

        currentKey = 1
        for key, value in self.models:
            if (value == name):
                currentKey = key

        conn = sqlite3.connect(PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT CoefficientType.Name, Coefficient.Value "
                       f"FROM Coefficient "
                       f"JOIN ModelCoefficient "
                       f"ON Coefficient.IdCoefficient = ModelCoefficient.IdCoefficient "
                       f"JOIN CoefficientType "
                       f"ON Coefficient.IdCoefficientType = CoefficientType.IdCoefficientType "
                       f"WHERE IdModel == '{currentKey}'")

        params_row = cursor.fetchall()
        for row_id in range(len(params_row)):
            self.coefficients[params_row[row_id][0]] = params_row[row_id][1]

        return self.coefficients





