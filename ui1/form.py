# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(487, 600)
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(9, 288, 103, 24))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Widget)
        self.checkBox.setGeometry(QtCore.QRect(247, 290, 108, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_prg = QtWidgets.QCheckBox(Widget)
        self.checkBox_prg.setGeometry(QtCore.QRect(380, 290, 75, 20))
        self.checkBox_prg.setObjectName("checkBox_prg")
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 330, 361, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.buttonReadLine = QtWidgets.QPushButton(Widget)
        self.buttonReadLine.setGeometry(QtCore.QRect(400, 330, 75, 24))
        self.buttonReadLine.setObjectName("buttonReadLine")

        self.retranslateUi(Widget)
        self.pushButton.clicked.connect(self.checkBox.toggle) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "name pushButton"))
        self.checkBox.setText(_translate("Widget", "name CheckBox"))
        self.checkBox_prg.setText(_translate("Widget", "from program"))
        self.buttonReadLine.setText(_translate("Widget", "Read Line"))
