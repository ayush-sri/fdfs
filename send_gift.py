# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sendgift.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sendGiftFrame(object):
    def setupUi(self, sendGiftFrame):
        sendGiftFrame.setObjectName("sendGiftFrame")
        sendGiftFrame.resize(494, 488)
        sendGiftFrame.setFixedSize(494,488)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/res/mail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sendGiftFrame.setWindowIcon(icon)
        sendGiftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        sendGiftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main = QtWidgets.QLabel(sendGiftFrame)
        self.main.setGeometry(QtCore.QRect(-5, -8, 511, 511))
        self.main.setStyleSheet("background-image: url(:/newPrefix/res/gift.png);")
        self.main.setText("")
        self.main.setObjectName("main")
        self.overlay = QtWidgets.QLabel(sendGiftFrame)
        self.overlay.setGeometry(QtCore.QRect(50, 30, 391, 361))
        self.overlay.setBaseSize(QtCore.QSize(500, 500))
        self.overlay.setStyleSheet("background-color: rgba(255, 255, 255, 190);")
        self.overlay.setText("")
        self.overlay.setObjectName("overlay")
        self.sendagift_label = QtWidgets.QLabel(sendGiftFrame)
        self.sendagift_label.setGeometry(QtCore.QRect(160, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        self.sendagift_label.setFont(font)
        self.sendagift_label.setObjectName("sendagift_label")
        self.email_edit = QtWidgets.QLineEdit(sendGiftFrame)
        self.email_edit.setGeometry(QtCore.QRect(160, 130, 181, 31))
        self.email_edit.setObjectName("email_edit")
        self.send_btn = QtWidgets.QPushButton(sendGiftFrame)
        self.send_btn.setGeometry(QtCore.QRect(200, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.send_btn.setFont(font)
        self.send_btn.setObjectName("send_btn")
        self.message_edit = QtWidgets.QLineEdit(sendGiftFrame)
        self.message_edit.setGeometry(QtCore.QRect(160, 190, 181, 31))
        self.message_edit.setObjectName("message_edit")

        self.retranslateUi(sendGiftFrame)
        QtCore.QMetaObject.connectSlotsByName(sendGiftFrame)

    def retranslateUi(self, sendGiftFrame):
        _translate = QtCore.QCoreApplication.translate
        sendGiftFrame.setWindowTitle(_translate("sendGiftFrame", "Send a gift"))
        self.sendagift_label.setText(_translate("sendGiftFrame", "SEND A GIFT"))
        self.email_edit.setPlaceholderText(_translate("sendGiftFrame", "Enter Email"))
        self.send_btn.setText(_translate("sendGiftFrame", "SEND"))
        self.message_edit.setPlaceholderText(_translate("sendGiftFrame", "Enter the message"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sendGiftFrame = QtWidgets.QFrame()
    ui = Ui_sendGiftFrame()
    ui.setupUi(sendGiftFrame)
    sendGiftFrame.show()
    sys.exit(app.exec_())

