# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from dbconnect import Dbconnection

class addReview(object):

    def addReview(self):
        movie=self.txtname.toPlainText()
        rating=self.cmbrating.currentText()
        email=self.plainTextEdit_4.toPlainText()



        con = Dbconnection.createConnection()
        strsql = "insert into reviews values (%s,%s,%s)"
        dbcon = con.cursor()
        dbcon.execute(strsql,(movie,rating,email))
        con.commit()
        con.close()
      #  print("review added")

    def showmessage(self):
        message = QMessageBox()
        message.setWindowTitle("Review")

        message.setText("Data Inserted")
        message.buttonClicked.connect(self.addReview)

        # message.setIcon(QMessageBox.Information)
        # message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # message.buttonClicked.connect(self.dlgbtn)
        message.exec()

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(591, 577)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblname = QtWidgets.QLabel(Frame)
        self.lblname.setGeometry(QtCore.QRect(60, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblname.setFont(font)
        self.lblname.setObjectName("lblname")
        self.txtname = QtWidgets.QPlainTextEdit(Frame)
        self.txtname.setGeometry(QtCore.QRect(250, 210, 191, 31))
        self.txtname.setObjectName("txtname")
        self.lblrating = QtWidgets.QLabel(Frame)
        self.lblrating.setGeometry(QtCore.QRect(60, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblrating.setFont(font)
        self.lblrating.setObjectName("lblrating")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(40, 390, 161, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(Frame)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(250, 380, 191, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 480, 76, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.showmessage)


        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(160, 0, 270, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 611, 621))
        self.label_2.setStyleSheet("background-image: url(:/resource/review2.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.cmbrating = QtWidgets.QComboBox(Frame)
        self.cmbrating.setGeometry(QtCore.QRect(250, 290, 69, 31))
        self.cmbrating.setObjectName("cmbrating")

        #manual
        self.cmbrating.addItem("1")
        self.cmbrating.addItem("1.5")
        self.cmbrating.addItem("2")
        self.cmbrating.addItem("2.5")
        self.cmbrating.addItem("3")
        self.cmbrating.addItem("3.5")
        self.cmbrating.addItem("4")
        self.cmbrating.addItem("4.5")
        self.cmbrating.addItem("5")



        self.label_2.raise_()
        self.lblname.raise_()
        self.txtname.raise_()
        self.lblrating.raise_()
        self.label_5.raise_()
        self.plainTextEdit_4.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.cmbrating.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.lblname.setText(_translate("Frame", "Movie Name"))
        self.lblrating.setText(_translate("Frame", "Rating"))
        self.label_5.setText(_translate("Frame", "Viewer Mail id"))
        self.pushButton.setText(_translate("Frame", "Submit"))
        self.label.setText(_translate("Frame", "   MOVIE REVIEW"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = addReview()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

