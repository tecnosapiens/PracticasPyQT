import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox
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
        # Controla el Evento Click
        self.ui.pbAceptarSesion.clicked.connect(self.fnProcesaClickAceptarSesion)



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

                if(event.key() == QtCore.Qt.Key_Return):
                    # Llama a la funcion para validar los datos 
                    self.fnValidaDatos()
    

    def fnProcesaClickAceptarSesion(self):
        if(self.ui.pbAceptarSesion.hasFocus()):
            # Llama a la funcion Validar los datos 
            self.fnValidaDatos()

    # FUNCION PARA VALIDAR LOS DATOS DEL DIALOGO DE INICIO DE SESION 
    def fnValidaDatos(self):
        # Variable para el mensaje
        sMensaje = ""

        # Valida el Usuario 
        if(len(self.ui.leUsuarioSesion.text())== 0):
            #Coloca el dato en el dialogo de mensaje 
            sMensaje =  "El usuario \n"

            # Coloca el foco en el usuario
            self.ui.leUsuarioSesion.setFocus()

        # Valida el Password
        if(len(self.ui.lePasswordSesion.text())==0):
            # Verifica si debe colocar el foco 
            if(len(sMensaje)==0):
                # Coloca el foco
                self.ui.lePasswordSesion.setFocus()

            # Agrega el dato en el sMensaje
            sMensaje = sMensaje + "El Password"
        # Verifica si debe desplegar el mensaje de erro 
        if(len(sMensaje)>0):
            # Actualiza el mensaje 
            sMensaje = "Revise los siguientes datos:\n"
            # Despliega el MessageBox
            fnMensaje(sMensaje, "El Usuario y el Password no pueden quedar vacios")
            # Hay error en los datos 
            return False
        else:
            # Despliega el MessageBox
            fnMensaje("Los datos estan correctos", "La plicación intentará el acceso")
            # los datos estan correctos
            return True


        # Valida en Usuario


        
def fnMensaje(sMensaje, sInformacion):
    #Crea un MessageBox
    msg = QMessageBox()

    # Establece el Icono
    msg.setIcon(QMessageBox.information)

    # Coloca el mensaje a desplegar definido por desarrollador
    msg.setText(sMensaje)
    msg.setInformativeText(sInformacion)
    msg.setWindowTitle("RoTech PyQt5")
    msg.setDetailedText("Los detalles encontrados son los siguientes")
    msg.setStandardButtons(QMessageBox.Ok)

    # Ejecuta el MessageBox
    msg.exec_()
    return
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = GUI_DialogoInicioSesion()
    myapp.show()
    sys.exit(app.exec_())