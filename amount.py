#coding:utf-8

# 必要的系統模組
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

import sys

# 自訂的模組
import gui
import loadup_thread
import loaddown_thread
import amount_thread
import amount_search

class Main(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        global dateRange

        self.pushButton_loadUP.clicked.connect(lambda: self.StartLoadUP())
        self.pushButton_loadDOWN.clicked.connect(lambda: self.StartLoadDOWN())
        self.pushButton_amount.clicked.connect(lambda: self.StartAmount())

    def StartLoadUP(self):
        loadup_thread.times = int(self.lineEdit_loadUP.text())

        self.progressBar_loadUP.setValue(0)
        self.listWidget_loadUP.addItem("===START===")
        self.trdLoadUP = loadup_thread.StartThreadFunc(self)
        self.trdLoadUP.start()

        print("fff")

    def StartLoadDOWN(self):
        loaddown_thread.times = int(self.lineEdit_loadDOWN.text())

        self.progressBar_loadDOWN.setValue(0)
        self.listWidget_loadDOWN.addItem("===START===")
        self.trdLoadDOWN = loaddown_thread.StartThreadFunc(self)
        self.trdLoadDOWN.start()

    def StartAmount(self):
        amount_thread.times = int(self.lineEdit_amount.text())

        self.progressBar_amount.setValue(0)
        self.listWidget_amount.addItem("===START===")
        self.trdProcess = amount_thread.StartThreadFunc(self)
        self.trdProcess.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())