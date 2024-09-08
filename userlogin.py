# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_Login(object):
    def runQuery(self,userid,password,role):
        selectQuery = "Select * from login where role="+role+"AND "
    def showMessage(self,messages):
        message = QMessageBox()
        message.setWindowTitle("Login")
        message.setText(messages)
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.exec()
    def login(self):
        userid = self.txtid.text()
        userpass = self.txtpass.text()
        role = self.cmblogin.currentText()

        if len(userid) == 0:
            self.showMessage("userid can not be null")

        elif len(userpass) == 0:
            self.showMessage("password can not be null")

        elif role == "login as":
             self.showMessage("please select role")

        else :
            runQuery(userid,userpass,role)

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(709, 566)
        Login.setFixedSize(700,500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/res/811804_cinema_512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-image: url(:/newPrefix/res/bg popcorn.png);")
        Login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(10, 71, 16, 16))
        self.label.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"background-image: url(:/resource/bg popcorn.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.cmblogin = QtWidgets.QComboBox(Login)
        self.cmblogin.setGeometry(QtCore.QRect(260, 130, 151, 31))
        self.cmblogin.setObjectName("cmblogin")
        self.cmblogin.addItem("login as")
        self.cmblogin.addItem("admin")
        self.cmblogin.addItem("manager")
        self.txtid = QtWidgets.QLineEdit(Login)
        self.txtid.setGeometry(QtCore.QRect(260, 180, 151, 41))
        self.txtid.setObjectName("txtid")
        self.txtpass = QtWidgets.QLineEdit(Login)
        self.txtpass.setGeometry(QtCore.QRect(260, 240, 151, 41))
        self.txtpass.setObjectName("txtpass")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(10, 285, 16, 16))
        self.label_2.setStyleSheet("image: url(:/resource/login icon.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btnsubmit = QtWidgets.QPushButton(Login)
        self.btnsubmit.setGeometry(QtCore.QRect(270, 330, 131, 32))
        self.btnsubmit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 255);\n"
"")
        self.btnsubmit.clicked.connect(self.login)
        self.btnsubmit.setObjectName("btnsubmit")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(270, 50, 141, 55))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 127);\n"
"\n"
"")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/res/bg popcorn.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Login)
        self.label_5.setGeometry(QtCore.QRect(140, 20, 101, 101))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/res/login icon.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_4.raise_()
        self.label.raise_()
        self.cmblogin.raise_()
        self.txtid.raise_()
        self.txtpass.raise_()
        self.label_2.raise_()
        self.btnsubmit.raise_()
        self.label_3.raise_()
        self.label_5.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login to continue"))
        self.txtid.setPlaceholderText(_translate("Login", "enter ID"))
        self.txtpass.setPlaceholderText(_translate("Login", "Enter Passsword"))
        self.btnsubmit.setText(_translate("Login", "Submit"))
        self.label_3.setText(_translate("Login", "LOGIN"))

import myresources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QFrame()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

