# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from lib.ui.Second_Window import Second_Window

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 757)
        with open("lib\\ui\\stylesheet.css", "r") as f:
            self.setStyleSheet(f.read())
        self.setWindowTitle("Open Overdrive Pipeline")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.createbutton = QPushButton("Create", self.centralwidget)
        self.deletebutton = QPushButton("Delete", self.centralwidget)
        self.listView = QListWidget(self.centralwidget)
        self.deletebutton.setGeometry(QRect(70, 340, 75, 23))
        self.createbutton.setGeometry(QRect(150, 340, 75, 23))
        self.listView.setGeometry(QRect(70, 71, 256, 241))
        self.createbutton.clicked.connect(self.create_new_asset)

    def create_new_asset(self):
        self.update_dialog = Second_Window("New Asset")
        self.update_dialog.show()




