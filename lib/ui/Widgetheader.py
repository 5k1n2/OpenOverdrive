# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widgetheader.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Widgetheader_ui(QMainWindow):
    def __init__(self):
        super(Widgetheader_ui, self).__init__()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setMinimumHeight(45)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setText("More")
        self.pushButton.setMinimumWidth(100)
        self.pushButton.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)



        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap("icons\\add.svg"))

        self.main_layout = QHBoxLayout()

        self.main_layout.addWidget(self.label, Qt.AlignLeft)
        self.main_layout.addWidget(self.pushButton)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.main_layout.setContentsMargins(20, 4, 4, 4)

        with open("lib\\ui\\stylesheet.css", "r") as f:
            self.setStyleSheet(f.read())



        QMetaObject.connectSlotsByName(self)
    # setupUi


    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)

    temp = Widgetheader_ui()
    temp.show()

    app.exec_()
    sys.exit(0)