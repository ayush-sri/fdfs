# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from dbconnect import Dbconnection


class Review(object):

    def addReview(self):
        movie=self.txtname.toPlainText()
        actor=self.txtactor.toPlainText()
        rating=self.cmbrating.currentText()
        date=self.cmbdate.currentText()
        month=self.cmbmonth.currentText()

        email=self.txtmail.toPlainText()



        con = Dbconnection.createConnection()
        strsql = "insert into reviews values (%s,%s,%s,%s,%s,%s)"
        dbcon = con.cursor()
        dbcon.execute(strsql,(movie,actor,rating,date,month,email))
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
        self.lblrating.setGeometry(QtCore.QRect(60, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblrating.setFont(font)
        self.lblrating.setObjectName("lblrating")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(30, 470, 161, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtmail = QtWidgets.QPlainTextEdit(Frame)
        self.txtmail.setGeometry(QtCore.QRect(250, 460, 191, 31))
        self.txtmail.setObjectName("txtmail")
        self.btnsubmit = QtWidgets.QPushButton(Frame)
        self.btnsubmit.setGeometry(QtCore.QRect(230, 530, 76, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setItalic(True)
        self.btnsubmit.setFont(font)
        self.btnsubmit.setObjectName("btnsubmit")

        self.btnsubmit.clicked.connect(self.showmessage)

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
        self.label_2.setGeometry(QtCore.QRect(0, 0, 611, 621))
        self.label_2.setStyleSheet("background-image: url(:/resource/review2.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.cmbrating = QtWidgets.QComboBox(Frame)
        self.cmbrating.setGeometry(QtCore.QRect(250, 340, 69, 31))
        self.cmbrating.setObjectName("cmbrating")

        # manual
        self.cmbrating.addItem("1")
        self.cmbrating.addItem("2")
        self.cmbrating.addItem("3")
        self.cmbrating.addItem("4")
        self.cmbrating.addItem("5")


        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 111, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtactor = QtWidgets.QPlainTextEdit(Frame)
        self.txtactor.setGeometry(QtCore.QRect(250, 270, 191, 31))
        self.txtactor.setToolTipDuration(-1)
        self.txtactor.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtactor.setObjectName("txtactor")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(60, 400, 141, 41))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cmbdate = QtWidgets.QComboBox(Frame)
        self.cmbdate.setGeometry(QtCore.QRect(268, 410, 51, 22))
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
        self.cmbdate.addItem("8")
        self.cmbdate.addItem("29")
        self.cmbdate.addItem("30")
        self.cmbdate.addItem("31")

        self.cmbmonth = QtWidgets.QComboBox(Frame)
        self.cmbmonth.setGeometry(QtCore.QRect(350, 410, 51, 22))
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

        self.label_2.raise_()
        self.lblname.raise_()
        self.txtname.raise_()
        self.lblrating.raise_()
        self.label_5.raise_()
        self.txtmail.raise_()
        self.btnsubmit.raise_()
        self.label.raise_()
        self.cmbrating.raise_()
        self.label_3.raise_()
        self.txtactor.raise_()
        self.label_4.raise_()
        self.cmbdate.raise_()
        self.cmbmonth.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.lblname.setText(_translate("Frame", "Movie Name"))
        self.label_3.setText(_translate("Frame", "Actor"))

        self.lblrating.setText(_translate("Frame", "Rating"))
        self.label_4.setText(_translate("Frame", "Release Date"))
        self.label_5.setText(_translate("Frame", "Viewer Mail id"))
        self.btnsubmit.setText(_translate("Frame", "Submit"))
        self.label.setText(_translate("Frame", "   MOVIE REVIEW"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Review()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

