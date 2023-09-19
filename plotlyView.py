from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
import os, sys
# from plotly import graph_objs as go
from plotly.offline import plot
# from plotly.subplots import make_subplots

class PlotlyViewer(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, fig, title, exec=True):
        # Create a QApplication instance or use the existing one if it exists
        self.app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)

        super().__init__()

        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "temp.html"))
        plot(fig, filename=self.file_path, auto_open=False)
        self.load(QUrl.fromLocalFile(self.file_path))
        self.setWindowTitle(title)
        self.show()

        if exec:
            self.app.exec_()
        while True:
            # Бесконечный цикл, чтобы удерживать окно открытым
            self.app.processEvents()

    def closeEvent(self, event):
        os.remove(self.file_path)