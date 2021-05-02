from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from lib.ui.Widgetheader import Widgetheader_ui
from lib.ui.Custom_Asset_Widgets import Dropdown_Selection, Text_Edit, CustomCheckbox, CustomTextfield, CustomDate

class Second_Window(QMainWindow):
    def __init__(self, Window_Title):
        super(Second_Window, self).__init__()
        self.resize(600, 700)

        with open("lib\\ui\\stylesheet.css", "r") as f:
            self.setStyleSheet(f.read())

        self.central_widget = QWidget()
        self.setWindowTitle(Window_Title)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(1)
        self.central_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.central_widget)

        self.create_header()

        self.item_holder = QWidget()
        self.item_holder_layout = QVBoxLayout()
        self.item_holder.setLayout(self.item_holder_layout)
        self.item_holder_layout.setContentsMargins(50,10,10,10)
        self.main_layout.addWidget(self.item_holder)

        self.create_text_edit("Name")
        self.create_dropdown("Genre")
        self.create_text_edit("Tags", "Greek, France, German")
        self.create_dropdown("Progress State")
        self.create_checkbox("UDIM")
        self.create_checkbox("SubD")
        self.create_checkbox("Author")
        self.create_textfield("Description")
        self.create_dropdown("Assigned to")
        self.create_dropdown("Target")
        self.create_text_edit("Texel Density")
        self.create_dropdown("Library")
        self.create_dropdown("Detail Level")
        self.create_text_edit("Polycount")
        self.create_dropdown("File")
        self.create_date("Due date")

        self.main_layout.setContentsMargins(0,0,0,0)




    def create_header(self):

        self.topheader = Widgetheader_ui()
        self.main_layout.addWidget(self.topheader,1, Qt.AlignTop)


    def create_dropdown(self, label_name):

        self.dropdown = Dropdown_Selection(label_name)
        self.item_holder_layout.addWidget(self.dropdown, 1)

    def create_text_edit(self, label_name, placeholder=None):

        self.Text_Edit = Text_Edit(label_name, placeholder)
        self.item_holder_layout.addWidget(self.Text_Edit, 1)

    def create_checkbox(self, label_name):

        self.checkbox = CustomCheckbox(label_name)
        self.item_holder_layout.addWidget(self.checkbox, 1)

    def create_textfield(self, label_name):
        self.textfield = CustomTextfield(label_name)
        self.item_holder_layout.addWidget(self.textfield, 1)

    def create_date(self, label_name):
        self.date = CustomDate(label_name)
        self.item_holder_layout.addWidget(self.date)