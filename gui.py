# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(740, 20, 331, 451))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget_amount = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_amount.setGeometry(QtCore.QRect(20, 70, 291, 261))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(8)
        self.listWidget_amount.setFont(font)
        self.listWidget_amount.setObjectName("listWidget_amount")
        self.pushButton_amount = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_amount.setGeometry(QtCore.QRect(110, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_amount.setFont(font)
        self.pushButton_amount.setStyleSheet("background-color: rgb(1, 19, 136);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_amount.setObjectName("pushButton_amount")
        self.progressBar_amount = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_amount.setGeometry(QtCore.QRect(27, 410, 291, 23))
        self.progressBar_amount.setProperty("value", 0)
        self.progressBar_amount.setObjectName("progressBar_amount")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(130, 40, 31, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_amount = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_amount.setGeometry(QtCore.QRect(70, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_amount.setFont(font)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 61, 21))
        self.label_6.setObjectName("label_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(18, 20, 331, 451))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.listWidget_loadUP = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_loadUP.setGeometry(QtCore.QRect(20, 70, 291, 261))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(8)
        self.listWidget_loadUP.setFont(font)
        self.listWidget_loadUP.setObjectName("listWidget_loadUP")
        self.pushButton_loadUP = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_loadUP.setGeometry(QtCore.QRect(110, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_loadUP.setFont(font)
        self.pushButton_loadUP.setStyleSheet("background-color: rgb(1, 19, 136);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_loadUP.setObjectName("pushButton_loadUP")
        self.progressBar_loadUP = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar_loadUP.setGeometry(QtCore.QRect(27, 410, 291, 23))
        self.progressBar_loadUP.setProperty("value", 0)
        self.progressBar_loadUP.setObjectName("progressBar_loadUP")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(130, 40, 31, 21))
        self.label.setObjectName("label")
        self.lineEdit_loadUP = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_loadUP.setGeometry(QtCore.QRect(70, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_loadUP.setFont(font)
        self.lineEdit_loadUP.setObjectName("lineEdit_loadUP")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 61, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(390, 20, 331, 451))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.listWidget_loadDOWN = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_loadDOWN.setGeometry(QtCore.QRect(20, 70, 291, 261))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(8)
        self.listWidget_loadDOWN.setFont(font)
        self.listWidget_loadDOWN.setObjectName("listWidget_loadDOWN")
        self.pushButton_loadDOWN = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_loadDOWN.setGeometry(QtCore.QRect(110, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_loadDOWN.setFont(font)
        self.pushButton_loadDOWN.setStyleSheet("background-color: rgb(1, 19, 136);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_loadDOWN.setObjectName("pushButton_loadDOWN")
        self.progressBar_loadDOWN = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_loadDOWN.setGeometry(QtCore.QRect(27, 410, 291, 23))
        self.progressBar_loadDOWN.setProperty("value", 0)
        self.progressBar_loadDOWN.setObjectName("progressBar_loadDOWN")
        self.lineEdit_loadDOWN = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_loadDOWN.setGeometry(QtCore.QRect(70, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_loadDOWN.setFont(font)
        self.lineEdit_loadDOWN.setObjectName("lineEdit_loadDOWN")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 61, 21))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.actionAmount = QtWidgets.QAction(MainWindow)
        self.actionAmount.setObjectName("actionAmount")
        self.actionUp_stock = QtWidgets.QAction(MainWindow)
        self.actionUp_stock.setObjectName("actionUp_stock")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "主力量價表"))
        self.pushButton_amount.setText(_translate("MainWindow", "開始下載"))
        self.label_3.setText(_translate("MainWindow", "天"))
        self.lineEdit_amount.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "新增"))
        self.groupBox_4.setTitle(_translate("MainWindow", "上市股票"))
        self.pushButton_loadUP.setText(_translate("MainWindow", "開始下載"))
        self.label.setText(_translate("MainWindow", "天"))
        self.lineEdit_loadUP.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "新增"))
        self.groupBox_5.setTitle(_translate("MainWindow", "上櫃股票"))
        self.pushButton_loadDOWN.setText(_translate("MainWindow", "開始下載"))
        self.lineEdit_loadDOWN.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "天"))
        self.label_5.setText(_translate("MainWindow", "新增"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.actionAmount.setText(_translate("MainWindow", "Amount"))
        self.actionUp_stock.setText(_translate("MainWindow", "Up-stock"))

