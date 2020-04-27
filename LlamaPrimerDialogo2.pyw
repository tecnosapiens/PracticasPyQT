import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from InicioSesionDialogo import *

class GUI_DialogoInicioSesion(QDialog) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_dlgSesion()
        self.ui.setupUi(self)

       # self.ui.leUsuarioSesion.returnPressed.connect(self.fnProcesarCambioTexto)

def fnProcesarCambioTexto():
    print("se presiono una tecla")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = GUI_DialogoInicioSesion()
    myapp.show()
    sys.exit(app.exec_())