# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_sale.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 196)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 60, 351, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setStyleSheet("background-color: #F6F7F9;\n"
"border: 1px solid #D1D2D4;\n"
"border-radius: 5%;")
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setStyleSheet("background-color: #F6F7F9;\n"
"border: 1px solid #D1D2D4;\n"
"border-radius: 5%;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 120, 28))
        self.pushButton.setMinimumSize(QtCore.QSize(120, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 5%;\n"
"background-color: #5394FD;\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 381, 151))
        self.frame.setStyleSheet("background-color: white;\n"
"border-radius: 5%;\n"
"border: 1px solid #D1D2D4")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(-10, -10, 431, 221))
        self.frame_2.setStyleSheet("background-image: url(:/backs/back-image.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        self.formLayoutWidget.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Пользователь"))
        self.label_2.setText(_translate("Form", "Товар"))
        self.label_4.setText(_translate("Form", "Добавление продажи"))
        self.pushButton.setText(_translate("Form", "Ввод"))
import res_rc
