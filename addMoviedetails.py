# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adddetails.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from dbconnect import Dbconnection


class AddMovieDetails(object):

    def addDetails(self):
        movie=self.txtname.text()
        actor=self.txtactor.text()
        genere=self.txtgenere.text()
        date=self.cmbdate.currentText()
        month=self.cmbmonth.currentText()
        year=self.cmbyear.currentText()

        if not len(movie)>0:
            print("enter movie name")

        else:

            con = Dbconnection.createConnection()
            strsql = "insert into moviedetails values (%s,%s,%s,%s,%s,%s)"
            dbcon = con.cursor()
            dbcon.execute(strsql,(movie,actor,genere,date,month,year))
            con.commit()
            con.close()
      #  print("review added")

    def showmessage(self):
        message = QMessageBox()
        message.setWindowTitle("Review")

        message.setText("Data Inserted")
        message.buttonClicked.connect(self.addDetails)

        # message.setIcon(QMessageBox.Information)
        # message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # message.buttonClicked.connect(self.dlgbtn)
        message.exec()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 595, 600))
        self.label.setStyleSheet("background-image: url(:/resource/6lvp4zT.jpg);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 170, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lblname = QtWidgets.QLabel(self.centralwidget)
        self.lblname.setGeometry(QtCore.QRect(110, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lblname.setFont(font)
        self.lblname.setStyleSheet(";\n"
"font: 75 14pt \"Rockwell\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lblname.setObjectName("lblname")
        self.lblactor = QtWidgets.QLabel(self.centralwidget)
        self.lblactor.setGeometry(QtCore.QRect(110, 240, 91, 31))
        self.lblactor.setStyleSheet(";\n"
"font: 75 14pt \"Rockwell\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lblactor.setObjectName("lblactor")
        self.lblgenere = QtWidgets.QLabel(self.centralwidget)
        self.lblgenere.setGeometry(QtCore.QRect(110, 320, 91, 31))
        self.lblgenere.setStyleSheet(";\n"
"font: 75 14pt \"Rockwell\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lblgenere.setObjectName("lblgenere")
        self.lbldatetime = QtWidgets.QLabel(self.centralwidget)
        self.lbldatetime.setGeometry(QtCore.QRect(80, 410, 151, 31))
        self.lbldatetime.setStyleSheet(";\n"
"font: 75 14pt \"Rockwell\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lbldatetime.setObjectName("lbldatetime")
        self.btnsubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnsubmit.setGeometry(QtCore.QRect(240, 510, 91, 41))
        self.btnsubmit.setStyleSheet(";\n"
"font: 75 14pt \"Rockwell\";\n"
"color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.btnsubmit.setObjectName("btnsubmit")

        self.btnsubmit.clicked.connect(self.showmessage)

        self.txtname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtname.setGeometry(QtCore.QRect(320, 150, 113, 31))
        self.txtname.setObjectName("txtname")
        self.txtactor = QtWidgets.QLineEdit(self.centralwidget)
        self.txtactor.setGeometry(QtCore.QRect(320, 240, 113, 31))
        self.txtactor.setObjectName("txtactor")
        self.txtgenere = QtWidgets.QLineEdit(self.centralwidget)
        self.txtgenere.setGeometry(QtCore.QRect(320, 320, 113, 31))
        self.txtgenere.setObjectName("txtgenere")
        self.cmbdate = QtWidgets.QComboBox(self.centralwidget)
        self.cmbdate.setGeometry(QtCore.QRect(280, 411, 51, 31))
        self.cmbdate.setObjectName("cmbdate")

        self.cmbdate.addItem("1")
        self.cmbdate.addItem("2")
        self.cmbdate.addItem("3")
        self.cmbdate.addItem("4")
        self.cmbdate.addItem("5")
        self.cmbdate.addItem("6")
        self.cmbdate.addItem("7")
        self.cmbdate.addItem("8")
        self.cmbdate.addItem("9")
        self.cmbdate.addItem("10")
        self.cmbdate.addItem("11")
        self.cmbdate.addItem("12")
        self.cmbdate.addItem("13")
        self.cmbdate.addItem("14")
        self.cmbdate.addItem("15")
        self.cmbdate.addItem("16")
        self.cmbdate.addItem("17")
        self.cmbdate.addItem("18")
        self.cmbdate.addItem("19")
        self.cmbdate.addItem("20")
        self.cmbdate.addItem("21")
        self.cmbdate.addItem("22")
        self.cmbdate.addItem("23")
        self.cmbdate.addItem("24")
        self.cmbdate.addItem("25")
        self.cmbdate.addItem("26")
        self.cmbdate.addItem("27")
        self.cmbdate.addItem("28")
        self.cmbdate.addItem("29")
        self.cmbdate.addItem("30")

        self.cmbmonth = QtWidgets.QComboBox(self.centralwidget)
        self.cmbmonth.setGeometry(QtCore.QRect(360, 410, 51, 31))
        self.cmbmonth.setObjectName("cmbmonth")

        self.cmbmonth.addItem("1")
        self.cmbmonth.addItem("2")
        self.cmbmonth.addItem("3")
        self.cmbmonth.addItem("4")
        self.cmbmonth.addItem("5")
        self.cmbmonth.addItem("6")
        self.cmbmonth.addItem("7")
        self.cmbmonth.addItem("8")
        self.cmbmonth.addItem("9")
        self.cmbmonth.addItem("10")
        self.cmbmonth.addItem("11")
        self.cmbmonth.addItem("12")

        self.cmbyear = QtWidgets.QComboBox(self.centralwidget)
        self.cmbyear.setGeometry(QtCore.QRect(430, 410, 51, 31))
        self.cmbyear.setObjectName("cmbyear")

        self.cmbyear.addItem("2018")
        self.cmbyear.addItem("2019")
        self.cmbyear.addItem("2020")
        self.cmbyear.addItem("2021")
        self.cmbyear.addItem("2022")
        self.cmbyear.addItem("2023")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "MOVIE DETAILS"))
        self.lblname.setText(_translate("MainWindow", "Name"))
        self.lblactor.setText(_translate("MainWindow", "Actor"))
        self.lblgenere.setText(_translate("MainWindow", "Genere"))
        self.lbldatetime.setText(_translate("MainWindow", "Releasing On"))
        self.btnsubmit.setText(_translate("MainWindow", "Submit"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AddMovieDetails()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

