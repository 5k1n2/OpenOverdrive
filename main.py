from PySide2.QtWidgets import QApplication, QWidget
import lib.ui.Main_Window
import sys


myApp = QApplication(sys.argv)
window = lib.ui.Main_Window.Ui_MainWindow()
window.setupUi(window)
window.show()
myApp.exec_()
sys.exit(0)