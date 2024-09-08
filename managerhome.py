 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbconnect import Dbconnection
from movieschart import Graph

from review import Review
from addMoviedetails import AddMovieDetails

class Ui_MainWindow(object):

    def addRatingform(self):
        self.MainWin = QtWidgets.QFrame()
        self.ui = Review()
        self.ui.setupUi(self.MainWin)  # making all the configuration of ui
        self.MainWin.show()
        #MainWindow.close()

    def moviegraph(self):

        self.MainWin = QtWidgets.QFrame()
        self.ui = Graph()
        self.ui.setupUi(self.MainWin)  # making all the configuration of ui
        self.MainWin.show()


    def addDetails(self):
        self.MainWin = QtWidgets.QMainWindow()
        self.ui = AddMovieDetails()
        self.ui.setupUi(self.MainWin)  # making all the configuration of ui
        self.MainWin.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 600)
        MainWindow.setStyleSheet("\n"
"background-image: url(:/resource/002-blurred-background-texture-vol2.jpg);\n"
"\n"
"color: rgb(0, 85, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 421, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 127);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 231, 411))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 150, 291, 421))
        self.label_2.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 0, 255);\n"
"color: rgb(0, 0, 127);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 61, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 61, 31))
        self.label_4.setStyleSheet("\n"
"color: rgb(170,0,  0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 61, 31))
        self.label_5.setStyleSheet("\n"
"color: rgb(170,0, 0);")
        self.label_5.setObjectName("label_5")
        self.txtid = QtWidgets.QTextEdit(self.centralwidget)
        self.txtid.setGeometry(QtCore.QRect(110, 260, 104, 31))
        self.txtid.setObjectName("txtid")
        self.txtname = QtWidgets.QTextEdit(self.centralwidget)
        self.txtname.setGeometry(QtCore.QRect(110, 340, 104, 31))
        self.txtname.setObjectName("txtname")
        self.txtcontact = QtWidgets.QTextEdit(self.centralwidget)
        self.txtcontact.setGeometry(QtCore.QRect(110, 420, 104, 31))
        self.txtcontact.setObjectName("txtcontact")
        self.btnadddetails = QtWidgets.QPushButton(self.centralwidget)
        self.btnadddetails.setGeometry(QtCore.QRect(360, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnadddetails.setFont(font)
        self.btnadddetails.setStyleSheet("color: rgb(0, 170, 0);\n"
"color: rgb(170, 0, 0);")
        self.btnadddetails.setObjectName("btnadddetails")

        self.btnadddetails.clicked.connect(self.addDetails)


        self.btneditprofile = QtWidgets.QPushButton(self.centralwidget)
        self.btneditprofile.setGeometry(QtCore.QRect(360, 240, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btneditprofile.setFont(font)
        self.btneditprofile.setStyleSheet("color: rgb(170,0, 0);")
        self.btneditprofile.setObjectName("btneditprofile")
        self.btnratingform = QtWidgets.QPushButton(self.centralwidget)
        self.btnratingform.setGeometry(QtCore.QRect(360, 310, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnratingform.setFont(font)
        self.btnratingform.setStyleSheet("color: rgb( 170,0, 0);")
        self.btnratingform.setObjectName("btnratingform")

        self.btnratingform.clicked.connect(self.addRatingform)

        self.btngraphactor = QtWidgets.QPushButton(self.centralwidget)
        self.btngraphactor.setGeometry(QtCore.QRect(360, 460, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btngraphactor.setFont(font)
        self.btngraphactor.setStyleSheet("color: rgb( 170,0, 0);")
        self.btngraphactor.setObjectName("btngraphactor")
        self.btnmoviegraph = QtWidgets.QPushButton(self.centralwidget)
        self.btnmoviegraph.setGeometry(QtCore.QRect(360, 380, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnmoviegraph.setFont(font)
        self.btnmoviegraph.setStyleSheet("color: rgb(170, 0, 0);")
        self.btnmoviegraph.setObjectName("btnmoviegraph")

        self.btnmoviegraph.clicked.connect(self.moviegraph)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "MANAGER PROFILE"))
        self.lineEdit_2.setText(_translate("MainWindow", "Personal Info"))
        self.label_3.setText(_translate("MainWindow", "Id"))
        self.label_4.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "Contact No"))
        self.btnadddetails.setText(_translate("MainWindow", "Add Movie Details"))
        self.btneditprofile.setText(_translate("MainWindow", "Edit Profile"))
        self.btnratingform.setText(_translate("MainWindow", "Movie Rating Form"))
        self.btngraphactor.setText(_translate("MainWindow", "Movie Graph By Actor"))
        self.btnmoviegraph.setText(_translate("MainWindow", "Movie Rating graph"))

import resources_rc
import myresources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

