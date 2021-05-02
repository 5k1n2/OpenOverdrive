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
        self.main_layout.addWidget(self.selectionlabel, 1)
        self.main_layout.setContentsMargins(10,10,10,0)

        self.dropdown = QComboBox()
        self.main_layout.addWidget(self.dropdown, 1)


class Text_Edit(QWidget):
    def __init__(self, Label_Text, placeholder=None):
        super(Text_Edit, self).__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.selectionlabel = QLabel()
        self.selectionlabel.setText(Label_Text)
        self.main_layout.addWidget(self.selectionlabel, 1)
        self.main_layout.setContentsMargins(10,10,10,0)

        self.Text_Edit = QLineEdit()
        self.Text_Edit.setPlaceholderText(placeholder)
        self.main_layout.addWidget(self.Text_Edit, 1)


class CustomCheckbox(QWidget):
    def __init__(self, label_text):
        super(CustomCheckbox, self).__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.selectionlabel = QLabel()
        self.selectionlabel.setText(label_text)
        self.main_layout.addWidget(self.selectionlabel, 1)
        self.main_layout.setContentsMargins(10,10,10,0)

        self.checkbox = QCheckBox()
        self.main_layout.addWidget(self.checkbox, 1)


class CustomTextfield(QWidget):
    def __init__(self, label_text):
        super(CustomTextfield, self).__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.selectionlabel = QLabel()
        self.selectionlabel.setText(label_text)
        self.main_layout.addWidget(self.selectionlabel, 1)
        self.main_layout.setContentsMargins(10,10,10,0)

        self.textedit = QTextEdit()
        self.main_layout.addWidget(self.textedit, 1)


class CustomDate(QWidget):
    def __init__(self, label_text):
        super(CustomDate, self).__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.selectionlabel = QLabel()
        self.selectionlabel.setText(label_text)
        self.main_layout.addWidget(self.selectionlabel, 1)
        self.main_layout.setContentsMargins(10,10,10,0)

        self.date = QCalendarWidget()
        self.main_layout.addWidget(self.date, 1)