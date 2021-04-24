from PySide2.QtWidgets import QApplication, QWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Title")
        self.setGeometry(300,300,300,300)



myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
sys.exit(0)