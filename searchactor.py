# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchactor.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from dbconnect import Dbconnection


class Ui_Frame(object):

    def addActor(self):

        con=Dbconnection.createConnection()
        strsql="select actor from reviews"
        dbcon = con.cursor()
        dbcon.execute(strsql)
        info = dbcon.fetchall()
        print(info)

        for data in info:
            self.cmbactor.cur





    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cmbactor = QtWidgets.QComboBox(Frame)
        self.cmbactor.setGeometry(QtCore.QRect(110, 50, 141, 22))
        self.cmbactor.setObjectName("cmbactor")


        self.btnloaddata = QtWidgets.QPushButton(Frame)
        self.btnloaddata.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.btnloaddata.setObjectName("btnloaddata")

        self.btnloaddata.clicked.connect(self.addActor)


        self.btnsubmit = QtWidgets.QPushButton(Frame)
        self.btnsubmit.setGeometry(QtCore.QRect(210, 140, 75, 23))
        self.btnsubmit.setObjectName("btnsubmit")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.btnloaddata.setText(_translate("Frame", "Load Data"))
        self.btnsubmit.setText(_translate("Frame", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

