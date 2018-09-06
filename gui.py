# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.winium_path = QtWidgets.QLineEdit(self.centralwidget)
        self.winium_path.setGeometry(QtCore.QRect(30, 40, 631, 20))
        self.winium_path.setObjectName("winium_path")
        self.stadiums_path = QtWidgets.QLineEdit(self.centralwidget)
        self.stadiums_path.setGeometry(QtCore.QRect(30, 100, 631, 20))
        self.stadiums_path.setObjectName("stadiums_path")
        self.auth_test_btn = QtWidgets.QPushButton(self.centralwidget)
        self.auth_test_btn.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.auth_test_btn.setObjectName("auth_test_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 221, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.auth_test_btn.setText(_translate("MainWindow", "Auth_Test"))
        self.label.setText(_translate("MainWindow", "Абсолютный путь к Winium"))
        self.label_2.setText(_translate("MainWindow", "Абсолютный путь к СОИ"))

window = Ui_MainWindow()