import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PrimeraVentana import *

class GUI_Principal(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI_Principal()
    myapp.show()
    sys.exit(app.exec_())