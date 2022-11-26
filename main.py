from PyQt5 import QtWidgets
from uifiles.pythonui import Ui_MainWindow
import sys
import requests 
import time

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time
import traceback, sys


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(tuple)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):

        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  
        finally:
            self.signals.finished.emit() 



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("WebhookSender")
        self.threadpool = QThreadPool()


        self.ui.pushButton_sair.clicked.connect(self.sair)
        self.ui.pushButton_enviar.clicked.connect(self.enviar)
          
    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("completado")
    
    def progress_fn(self, progress):
        p, m = (progress)
        print("%d%% done %s" % (p, m))

    def enviar_so_que_de_verdade(self, **kwargs):
        self.ui.pushButton_enviar.setEnabled(False)
        self.ui.pushButton_enviar.setStyleSheet("background-color: rgb(3, 25, 0);")
        
        r = requests.post(self.ui.lineEdit_URL.text(), data={"username": self.ui.lineEdit_Name.text(), "content": self.ui.lineEdit_Message.text()}  )
        self.setWindowTitle(f"WebhookSender - {r.status_code}")
        #background-color: rgb(6, 46, 0);
        self.ui.pushButton_enviar.setEnabled(True)
        self.ui.pushButton_enviar.setStyleSheet("background-color: rgb(6, 66, 0); color: rgb(255, 255, 255);")
        pass


    def sair(self):
        sys.exit()

    def enviar(self):
        worker = Worker(self.enviar_so_que_de_verdade)
        self.threadpool.start(worker)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        pass


def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     sys.exit(app.exec_())

if __name__ == "__main__":
     main()
