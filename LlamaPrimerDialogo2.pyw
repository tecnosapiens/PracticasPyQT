import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from MiPrimerDialogoQt import *

class GUI_Principal(QDialog) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = GUI_Principal()
    myapp.show()
    sys.exit(app.exec_())