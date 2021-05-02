from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Dropdown_Selection(QWidget):
    def __init__(self, Label_Text):
        super(Dropdown_Selection, self).__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.selectionlabel = QLabel()
        self.selectionlabel.setText(Label_Text)
        self.main_layout.addWidget(self.selectionlabel)

        self.dropdown = QComboBox()
        self.main_layout.addWidget((self.dropdown))