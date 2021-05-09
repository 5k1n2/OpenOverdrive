from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from lib.ui.Widgetheader import Widgetheader_ui
from lib.ui.Custom_Asset_Widgets import Dropdown_Selection, Text_Edit, CustomCheckbox, CustomTextfield, CustomDate
import asset
import jsonpickle, json

class Second_Window(QDialog):
    def __init__(self, Window_Title):
        super(Second_Window, self).__init__()
        self.resize(600, 700)

        with open("lib\\ui\\stylesheet.css", "r") as f:
            self.setStyleSheet(f.read())

        self.central_widget = QWidget()
        self.setWindowTitle(Window_Title)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(1)

        self.setLayout(self.main_layout)

        self.create_header()

        self.item_holder = QWidget()
        self.item_holder_layout = QVBoxLayout()
        self.item_holder.setLayout(self.item_holder_layout)
        self.item_holder_layout.setContentsMargins(50,10,10,10)
        self.main_layout.addWidget(self.item_holder)

        self.asset_name = self.create_text_edit("Name")
        self.asset_genre = self.create_dropdown("Genre")
        self.asset_tags = self.create_text_edit("Tags", "Greek, France, German")
        self.asset_progress = self.create_dropdown("Progress State")
        self.asset_udim = self.create_checkbox("UDIM")
        self.asset_subd = self.create_checkbox("SubD")
        self.asset_author = self.create_checkbox("Author")
        self.asset_description = self.create_textfield("Description")
        self.asset_assigned = self.create_dropdown("Assigned to")
        self.asset_target = self.create_dropdown("Target")
        self.asset_texel = self.create_text_edit("Texel Density")
        self.asset_library = self.create_dropdown("Library")
        self.asset_detail = self.create_dropdown("Detail Level")
        self.asset_polycount = self.create_text_edit("Polycount")
        self.asset_file = self.create_dropdown("File")
        self.asset_due = self.create_date("Due date")

        self.buttom_widget()

        self.main_layout.setContentsMargins(0,0,0,0)






    def create_header(self):

        self.topheader = Widgetheader_ui()
        self.main_layout.addWidget(self.topheader,1, Qt.AlignTop)


    def create_dropdown(self, label_name):

        self.dropdown = Dropdown_Selection(label_name)
        self.item_holder_layout.addWidget(self.dropdown, 1)
        return self.dropdown

    def create_text_edit(self, label_name, placeholder=None):

        self.Text_Edit = Text_Edit(label_name, placeholder)
        self.item_holder_layout.addWidget(self.Text_Edit, 1)
        return self.Text_Edit

    def create_checkbox(self, label_name):

        self.checkbox = CustomCheckbox(label_name)
        self.item_holder_layout.addWidget(self.checkbox, 1)
        return self.checkbox

    def create_textfield(self, label_name):
        self.textfield = CustomTextfield(label_name)
        self.item_holder_layout.addWidget(self.textfield, 1)
        return self.textfield

    def create_date(self, label_name):
        self.date = CustomDate(label_name)
        self.item_holder_layout.addWidget(self.date)
        return self.date

    def buttom_widget(self):

        self.buttom_layout = QHBoxLayout()

        self.cancelbutton = QPushButton(self)
        self.cancelbutton.setText("Cancel")
        self.cancelbutton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.cancelbutton.setMinimumHeight(30)
        self.cancelbutton.clicked.connect(self.close_window)

        self.acceptbutton = QPushButton(self)
        self.acceptbutton.setText("Accept")
        self.acceptbutton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.acceptbutton.setMinimumHeight(30)
        self.acceptbutton.clicked.connect(self.accept_asset)

        self.buttom_layout.addWidget(self.cancelbutton)
        self.buttom_layout.addWidget(self.acceptbutton)

        self.button_widget = QWidget()
        self.button_widget.setLayout(self.buttom_layout)

        self.main_layout.addWidget(self.button_widget)

    def accept_asset(self):



        # self.asset = asset.Asset(self.asset_name.get_Text(), self.asset_genre, self.asset_tags, self.asset_progress,
        #                          self.asset_udim,self.asset_subd, self.asset_author, self.asset_description,
        #                          self.asset_assigned, self.asset_target, self.asset_texel, self.asset_library,
        #                          self.asset_detail, self.asset_polycount, self.asset_file, self.asset_due)

        self.asset = asset.Asset(self.asset_name.get_Text())

        with open("data.json", 'w') as f:
            json_obj = jsonpickle.encode(self.asset, indent=5)
            f.write(json_obj)

    def close_window(self):
        self.close()