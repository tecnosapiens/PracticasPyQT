import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from InicioSesionDialogo import *

class GUI_DialogoInicioSesion(QDialog) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_dlgSesion()
        self.ui.setupUi(self)

        # CONTROL DE EVENTOS PARA EL CONTROL LINE EDIT leUsuarioSesion
        #Establece la funcion para cuando se presione enter en el en control Line Edit leUsuarioSesion
        self.ui.leUsuarioSesion.returnPressed.connect(self.fnProcesarEnter)

        # Establece la funcion procesar cambio de texto en control Line Edit leUsuarioSesion
        self.ui.leUsuarioSesion.keyPressEvent = self.keyPressEvent


         # CONTROL DE EVENTOS PARA EL CONTROL LINE EDIT leUsuarioSesion
        #Establece la funcion para cuando se presione enter en control Line Edit Password
        self.ui.lePasswordSesion.returnPressed.connect(self.fnProcesarEnter)

        # Establece la funcion procesar cambio de texto en control Line Edit Password
        self.ui.lePasswordSesion.textChanged.connect(self.fnProcesarCambioTexto)

          # Establece la funcion procesar un evento de presion de tecla sobre el control Line Edit Password
        self.ui.lePasswordSesion.keyPressEvent = self.keyPressEvent


        # CONTROL DE EVENTOS PARA EL CONTROL Boton Aceptar
        # Asocia el KeyPressEvent al Boton de Aceptar
        self.ui.pbAceptarSesion.keyPressEvent = self.keyPressEvent



    #FUNCIONES PARA LOS EVENTOS DE PRESION SOBRE CONTROLES    

    def fnProcesarEnter(self):
        print("has presionado ENTER")
        #Se verifica si tiene el foco el usuario 
        if(self.ui.leUsuarioSesion.hasFocus()):
            # manda el foco al pasword
            print("foco al Password")
            self.ui.lePasswordSesion.setFocus()
        else:
            #El foco lo tiene el password
            print("El foco a Aceptar")
            self.ui.pbAceptarSesion.setFocus()

    # Funcion para detectar cambios
    def fnProcesarCambioTexto(self):
        #Verifica si tiene el foco el usuario
        if(self.ui.leUsuarioSesion.hasFocus()):
            # manda el focus al password
            print("Cambio de texto en usuario")
            print(self.ui.leUsuarioSesion.text())
        else:
            #El foco lo tiene el password
            print("Cambio de Texto en Password")
            print(self.ui.lePasswordSesion.text())

    # Se ha presionado una tecla 
    def keyPressEvent(self, event):
        print("se ha presionado una tecla al inicio: ", event.text())
        
        # Verifica si tiene el foco el Usuario 
        if(self.ui.leUsuarioSesion.hasFocus()):
            # El Usuario tiene el Foco
            print("Estando en Usuario")
            # Evitando el 5
            if(event.text()!="5"):
                return QtWidgets.QLineEdit.keyPressEvent(self.ui.leUsuarioSesion, event)

        elif(self.ui.lePasswordSesion.hasFocus()):
            # El foco lo tiene el Password
            print("Estando en Password")
            if(event.text()!="7"):
                return QtWidgets.QLineEdit.keyPressEvent(self.ui.lePasswordSesion, event)
        else:
                # Mensaje
                print("Se presiono una tecla en el boton de Aceptar")
        

      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = GUI_DialogoInicioSesion()
    myapp.show()
    sys.exit(app.exec_())