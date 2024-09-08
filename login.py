# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from select import select

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Frame(object):

    def showMessage(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("login info")
        msg.setText(message)# to set value in msg box

        msg.setIcon(QMessageBox.Information)  # info is static var using qmegbox class name
        msg.setStandardButtons(QMessageBox.Ok)
        #msg.buttonClicked.connect(self.dlgButton)
        returnval=msg.exec_()  # to execute msg box


    def login(self):
        userid = self.txtid.text()
        userpass = self.txtpass.text()
        role=self.cmblogin.text()

        if not len(userid)>0:
            self.showMessage("userid can not be null")

        elif not len(userpass)>0:
            self.showMessage("password can not be null")

        elif not len(role)>0:
            self.showMessage("please enter role")




    def setupUi(self, Frame):
        Frame.setObjectName("Frame")

        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(0, -10, 801, 591))
        self.label.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"background-image: url(:/resource/bg popcorn.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.cmblogin = QtWidgets.QComboBox(Frame)
        self.cmblogin.setGeometry(QtCore.QRect(270, 210, 201, 41))
        self.cmblogin.setObjectName("cmblogin")

        self.cmblogin.addItem("login as")
        self.cmblogin.addItem("admin")

        self.cmblogin.addItem("manager")

        self.txtid = QtWidgets.QLineEdit(Frame)
        self.txtid.setGeometry(QtCore.QRect(270, 300, 201, 41))
        self.txtid.setObjectName("txtid")
        self.txtpass = QtWidgets.QLineEdit(Frame)
        self.txtpass.setGeometry(QtCore.QRect(270, 380, 201, 41))
        self.txtpass.setObjectName("txtpass")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 161, 181))
        self.label_2.setStyleSheet("image: url(:/resource/login icon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 281, 71))
        self.label_3.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 75 36pt \"Times New Roman\";\n"
"text-decoration: underline;")
        self.label_3.setObjectName("label_3")
        self.btnsubmit = QtWidgets.QPushButton(Frame)
        self.btnsubmit.setGeometry(QtCore.QRect(230, 470, 181, 41))
        self.btnsubmit.setStyleSheet("font: 75 14pt \"Trebuchet MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(170, 0, 0);")
        self.btnsubmit.setObjectName("btnsubmit")

        self.btnsubmit.clicked.connect(self.login)


        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.txtid.setPlaceholderText(_translate("Frame", "enter ID"))
        self.txtpass.setPlaceholderText(_translate("Frame", "Enter Passsword"))
        self.label_3.setText(_translate("Frame", "LOGIN"))
        self.btnsubmit.setText(_translate("Frame", "Submit"))

import resources_rc2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

