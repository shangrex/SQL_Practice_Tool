# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 868)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(880, 60, 161, 61))
        self.Search_btn.setObjectName("Search_btn")
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(90, 60, 771, 61))
        self.input_text.setObjectName("input_text")
        self.output_text = QtWidgets.QTextEdit(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(90, 170, 771, 661))
        self.output_text.setObjectName("output_text")
        self.Input_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Input_btn.setGeometry(QtCore.QRect(880, 170, 161, 71))
        self.Input_btn.setObjectName("Input_btn")
        self.Delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_btn.setGeometry(QtCore.QRect(880, 280, 161, 71))
        self.Delete_btn.setObjectName("Delete_btn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(880, 30, 161, 25))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Search_btn.setText(_translate("MainWindow", "Search"))
        self.Input_btn.setText(_translate("MainWindow", "Input_Data"))
        self.Delete_btn.setText(_translate("MainWindow", "Delete_Data"))
