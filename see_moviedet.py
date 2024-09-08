# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem


class seeMovieDetFrame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(321, 577)
        Frame.setFixedSize(321,577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/res/movdet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main = QtWidgets.QLabel(Frame)
        self.main.setGeometry(QtCore.QRect(0, 0, 251, 241))
        self.main.setStyleSheet("background-image: url(:/newPrefix/reel.png);")
        self.main.setText("")
        self.main.setObjectName("main")
        self.overlay = QtWidgets.QLabel(Frame)
        self.overlay.setGeometry(QtCore.QRect(-4, -8, 451, 241))
        self.overlay.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.overlay.setText("")
        self.overlay.setObjectName("overlay")
        self.filter_header = QtWidgets.QLabel(Frame)
        self.filter_header.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.filter_header.setFont(font)
        self.filter_header.setObjectName("filter_header")
        self.date = QtWidgets.QComboBox(Frame)
        self.date.setGeometry(QtCore.QRect(30, 80, 51, 22))
        self.date.setObjectName("date")
        for i in range(1,32):
            self.date.addItem(str(i))
        self.month = QtWidgets.QComboBox(Frame)
        self.month.setGeometry(QtCore.QRect(110, 80, 69, 22))
        self.month.setObjectName("month")
        for i in range(1,12):
            self.month.addItem(str(i))
        self.year = QtWidgets.QComboBox(Frame)
        self.year.setGeometry(QtCore.QRect(200, 80, 61, 22))
        self.year.setObjectName("year")
        for i in range(1948,2048):
            self.year.addItem(str(i))
        self.searchbyactor_edit = QtWidgets.QLineEdit(Frame)
        self.searchbyactor_edit.setGeometry(QtCore.QRect(50, 120, 181, 20))
        self.searchbyactor_edit.setObjectName("searchbyactor_edit")
        self.search_btn = QtWidgets.QPushButton(Frame)
        self.search_btn.setGeometry(QtCore.QRect(60, 170, 75, 23))
        self.search_btn.setObjectName("search_btn")
        self.salect_label = QtWidgets.QLabel(Frame)
        self.salect_label.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.salect_label.setObjectName("salect_label")
        self.all_btn = QtWidgets.QPushButton(Frame)
        self.all_btn.setGeometry(QtCore.QRect(180, 170, 75, 23))
        self.all_btn.setObjectName("all_btn")
        self.movieListHolder = QtWidgets.QScrollArea(Frame)
        self.movieListHolder.setGeometry(QtCore.QRect(-1, 239, 331, 331))
        self.movieListHolder.setWidgetResizable(True)
        self.movieListHolder.setObjectName("movieListHolder")
        self.movieListHolderWidget = QtWidgets.QWidget()
        self.movieListHolderWidget.setGeometry(QtCore.QRect(0, 0, 329, 329))
        self.movieListHolderWidget.setObjectName("movieListHolderWidget")
        self.movieList = QtWidgets.QListWidget(self.movieListHolderWidget)
        self.movieList.setGeometry(QtCore.QRect(0, 0, 321, 331))
        self.movieList.setObjectName("movieList")
        item = QListWidgetItem(QIcon(":/newPrefix/res/unnamed.png"),"DDLJ , SRK and KAJOL ,released on some date,rating : 5/5 ")
        self.movieList.addItem(item)
        self.movieList.addItem("DDLJ")
        self.movieList.addItem("DDLJ")
        self.movieList.addItem("DDLJ")
        self.movieList.addItem("DDLJ")
        self.movieList.addItem("DDLJ")
        self.movieListHolder.setWidget(self.movieListHolderWidget)
        self.movieListHolder.raise_()
        self.main.raise_()
        self.overlay.raise_()
        self.filter_header.raise_()
        self.date.raise_()
        self.month.raise_()
        self.year.raise_()
        self.searchbyactor_edit.raise_()
        self.search_btn.raise_()
        self.salect_label.raise_()
        self.all_btn.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "movie details"))
        self.filter_header.setText(_translate("Frame", "Filter"))
        self.searchbyactor_edit.setPlaceholderText(_translate("Frame", "search by actor name"))
        self.search_btn.setText(_translate("Frame", "Search"))
        self.salect_label.setText(_translate("Frame", "select date or month:"))
        self.all_btn.setText(_translate("Frame", "All movies"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = seeMovieDetFrame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

