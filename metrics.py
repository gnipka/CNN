import sklearn.metrics
import math
import numpy

REGALATORY_THRESHOLD = 75
PERCENT_OF_DEFECTS = 40

class metrics():
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
        self.TP, self.FP, self.TN, self.FN = self.get_classifiers(self.get_threshold(PERCENT_OF_DEFECTS))
        self.TPR = self.TP / (self.TP + self.FN)
        self.FPR = self.FP / (self.FP + self.TN)

    def mse(self):
        return sklearn.metrics.mean_squared_error(self.y_true, self.y_pred)

    def mae(self):
        return sklearn.metrics.mean_absolute_error(self.y_true, self.y_pred)

    def mape(self):
        return sklearn.metrics.mean_absolute_percentage_error(self.y_true, self.y_pred)

    def rmse(self):
        return math.sqrt(sklearn.metrics.mean_squared_error(self.y_true, self.y_pred))

    def precision(self):
        self.precision = self.TP / (self.TP + self.FP)
        return self.precision

    def recall(self):
        self.recall = self.TP / (self.TP + self.FN)
        return self.recall

    def f1(self):
        return 2 * ((self.precision * self.recall) / (self.precision + self.recall))

    def auc(self):
        self.TPR = []
        self.FPR = []

        thresholds = numpy.linspace(0, REGALATORY_THRESHOLD)

        for i in thresholds:
            tp, fp, tn, fn = self.get_classifiers(i)
            if (tp + fn) != 0:
                self.TPR.append(tp / (tp + fn))
            else:
                self.TPR.append(1)
            if (fp + tn) != 0:
                self.FPR.append(fp / (fp + tn))
            else:
                self.FPR.append(1)

        self.TPR.sort()
        self.FPR.sort()

        AUC = 0
        for i in range(len(thresholds) - 1):
            AUC = AUC + (((self.TPR[i] + self.TPR[i + 1]) / 2) * (self.FPR[i + 1] - self.FPR[i]))
        return AUC

    def r2(self):
        return sklearn.metrics.r2_score(self.y_true, self.y_pred)

    def get_classifiers(self, threshold):
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for i in range(len(self.y_pred)):
            if self.y_pred[i] >= threshold:
                if self.y_true[i] >= threshold:
                    TP = TP + 1
                else:
                    FP = FP + 1
            else:
                if self.y_true[i] < threshold:
                    TN = TN + 1
                else:
                    FN = FN + 1
        return (TP, FP, TN, FN)

    def get_threshold(self, percent):
        result = 0
        threshold = REGALATORY_THRESHOLD
        while result < percent:
            TP, FP, TN, FN = self.get_classifiers(threshold)
            result = ((TP + FN) / len(self.y_pred)) * 100
            threshold = threshold - 1
        return threshold






