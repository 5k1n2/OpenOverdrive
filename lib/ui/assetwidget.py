from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

class Assetwidget(QWidget):
    def __init__(self):
        super(Assetwidget, self).__init__()
        self.mainwidget = QWidget()
        self.mainlayout = QVBoxLayout()


        self.colorwidget = QWidget()
        pallete = self.palette()
        pallete.setColor(QPalette.Window, QColor(128, 0, 0))
        self.colorwidget.setPalette(pallete)
        self.colorwidget.setAutoFillBackground(True)
        self.setLayout(self.mainlayout)

        self.info_layout = self.set_main_info()

        self.mainlayout.addWidget(self.info_layout)
        self.mainlayout.addWidget(self.colorwidget)

    def set_main_info(self):




        data_layout = QVBoxLayout()

        name_label = QLabel()
        name_label.setText("Name")

        description_label = QLabel()
        description_label.setText("Description")

        data_layout.addWidget(name_label)
        data_layout.addWidget(description_label)

        preview_image = QLabel()
        preview_image.setPixmap(None)

        info_layout = QHBoxLayout()
        info_layout.addWidget(preview_image)
        info_layout.addLayout(data_layout)

        main_info_widget = QWidget()
        main_info_widget.setLayout(info_layout)

        return main_info_widget

    def set_color(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    temp = Assetwidget()
    temp.show()
    app.exec_()

