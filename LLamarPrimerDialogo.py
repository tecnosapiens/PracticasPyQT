import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QApplication



class ejemploGui(QDialog):
    def __init(self):
        super().__init()
        uic.loadUi("MiPrimerDialogoQt.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    GUI = ejemploGui()
    GUI.show()
    sys.exit(app.exec_())