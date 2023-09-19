# import sqlite3
#
# PATH = 'models.db'
#
# class dbModel:
#
#     def __init__(self):
#         self.models = dict()
#         self.coefficients = dict()
#
#     def loadNameModel(self):
#         conn = sqlite3.connect(PATH)
#         cursor = conn.cursor()
#         cursor.execute(f"SELECT *"
#                        f"FROM Model")
#         params_row = cursor.fetchall()
#         for row_id in range(len(params_row)):
#             self.models[params_row[row_id][0]] = params_row[row_id][1]
#         cursor.close()
#         conn.close()
#         return self.models
#
#     # def loadCoefficient(self, name):
#     #
#     #     currentKey = 1
#     #     for key, value in self.models:
#     #         if (value == name):
#     #             currentKey = key
#     #
#     #     conn = sqlite3.connect(PATH)
#     #     cursor = conn.cursor()
#     #     cursor.execute(f"SELECT SCICoefficientTypes.Name, SCICoefficients.Value "
#     #                    f"FROM SCICoefficients "
#     #                    f"JOIN SCIModelCoefficients "
#     #                    f"ON SCICoefficients.IdCoefficient = SCIModelCoefficients.IdCoefficient "
#     #                    f"JOIN SCICoefficientTypes "
#     #                    f"ON SCICoefficients.IdCoefficientType = SCICoefficientTypes.IdCoefficientType "
#     #                    f"WHERE IdModel == '{currentKey}'")
#     #
#     #     params_row = cursor.fetchall()
#     #     for row_id in range(len(params_row)):
#     #         self.coefficients[params_row[row_id][0]] = params_row[row_id][1]
#     #
#     #     return self.coefficients
#
#
#
#
#
