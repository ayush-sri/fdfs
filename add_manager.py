# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmanager.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddManager(object):
    def setupUi(self, AddManager):
        AddManager.setObjectName("AddManager")
        AddManager.resize(452, 427)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/res/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddManager.setWindowIcon(icon)
        AddManager.setFrameShape(QtWidgets.QFrame.StyledPanel)
        AddManager.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main = QtWidgets.QLabel(AddManager)
        self.main.setGeometry(QtCore.QRect(-4, -11, 671, 471))
        self.main.setStyleSheet("background-image: url(:/newPrefix/res/tv-interview-vector-illustration-vector-clipart_csp45553405.jpg);")
        self.main.setText("")
        self.main.setObjectName("main")
        self.name_edit = QtWidgets.QLineEdit(AddManager)
        self.name_edit.setGeometry(QtCore.QRect(150, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_edit.setFont(font)
        self.name_edit.setObjectName("name_edit")
        self.email_edit = QtWidgets.QLineEdit(AddManager)
        self.email_edit.setGeometry(QtCore.QRect(150, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email_edit.setFont(font)
        self.email_edit.setObjectName("email_edit")
        self.id_edit = QtWidgets.QLineEdit(AddManager)
        self.id_edit.setGeometry(QtCore.QRect(150, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_edit.setFont(font)
        self.id_edit.setObjectName("id_edit")
        self.contact_edit = QtWidgets.QLineEdit(AddManager)
        self.contact_edit.setGeometry(QtCore.QRect(150, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contact_edit.setFont(font)
        self.contact_edit.setObjectName("contact_edit")
        self.btn_submit = QtWidgets.QPushButton(AddManager)
        self.btn_submit.setGeometry(QtCore.QRect(160, 290, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_submit.setFont(font)
        self.btn_submit.setStyleSheet("background-color: rgb(225, 241, 238);\n"
"color: rgb(173, 184, 212);")
        self.btn_submit.setObjectName("btn_submit")
        self.overlay = QtWidgets.QLabel(AddManager)
        self.overlay.setGeometry(QtCore.QRect(-10, 0, 461, 431))
        self.overlay.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"")
        self.overlay.setText("")
        self.overlay.setObjectName("overlay")
        self.main.raise_()
        self.overlay.raise_()
        self.name_edit.raise_()
        self.email_edit.raise_()
        self.id_edit.raise_()
        self.contact_edit.raise_()
        self.btn_submit.raise_()

        self.retranslateUi(AddManager)
        QtCore.QMetaObject.connectSlotsByName(AddManager)

    def retranslateUi(self, AddManager):
        _translate = QtCore.QCoreApplication.translate
        AddManager.setWindowTitle(_translate("AddManager", "add manager"))
        self.name_edit.setPlaceholderText(_translate("AddManager", "Enter name"))
        self.email_edit.setPlaceholderText(_translate("AddManager", "Enter email address"))
        self.id_edit.setPlaceholderText(_translate("AddManager", "Enter id"))
        self.contact_edit.setPlaceholderText(_translate("AddManager", "Contact number"))
        self.btn_submit.setText(_translate("AddManager", "Submit"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddManager = QtWidgets.QFrame()
    ui = Ui_AddManager()
    ui.setupUi(AddManager)
    AddManager.show()
    sys.exit(app.exec_())

