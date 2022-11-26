# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './uifiles/a.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 206)
        MainWindow.setMinimumSize(QtCore.QSize(0, 185))
        MainWindow.setMaximumSize(QtCore.QSize(700, 400))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_URL = QtWidgets.QLabel(self.centralwidget)
        self.label_URL.setObjectName("label_URL")
        self.horizontalLayout_6.addWidget(self.label_URL)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.lineEdit_URL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_URL.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"")
        self.lineEdit_URL.setObjectName("lineEdit_URL")
        self.horizontalLayout_6.addWidget(self.lineEdit_URL)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Name.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"")
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.horizontalLayout.addWidget(self.lineEdit_Name)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.horizontalLayout_3.addWidget(self.label_message)
        spacerItem7 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.lineEdit_Message = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Message.setStyleSheet("background-color: rgb(26, 26, 26);\n"
"")
        self.lineEdit_Message.setObjectName("lineEdit_Message")
        self.horizontalLayout_3.addWidget(self.lineEdit_Message)
        spacerItem8 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enviar.setMinimumSize(QtCore.QSize(300, 0))
        self.pushButton_enviar.setStyleSheet("background-color: rgb(6, 66, 0);\n"
"")
        self.pushButton_enviar.setObjectName("pushButton_enviar")
        self.horizontalLayout_4.addWidget(self.pushButton_enviar)
        self.pushButton_sair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sair.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_sair.setStyleSheet("background-color: rgb(60, 0, 1);")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.horizontalLayout_4.addWidget(self.pushButton_sair)
        spacerItem9 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_URL.setText(_translate("MainWindow", "URL        "))
        self.label_name.setText(_translate("MainWindow", "Nome     "))
        self.label_message.setText(_translate("MainWindow", "Message"))
        self.pushButton_enviar.setText(_translate("MainWindow", "Enviar"))
        self.pushButton_sair.setText(_translate("MainWindow", "Sair"))