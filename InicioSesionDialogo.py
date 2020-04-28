# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\InicioSesionDialogo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgSesion(object):
    def setupUi(self, dlgSesion):
        dlgSesion.setObjectName("dlgSesion")
        dlgSesion.resize(439, 334)
        self.gbSesion = QtWidgets.QGroupBox(dlgSesion)
        self.gbSesion.setGeometry(QtCore.QRect(10, 10, 411, 241))
        self.gbSesion.setObjectName("gbSesion")
        self.lblUsuarioSesion = QtWidgets.QLabel(self.gbSesion)
        self.lblUsuarioSesion.setGeometry(QtCore.QRect(20, 30, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsuarioSesion.setFont(font)
        self.lblUsuarioSesion.setObjectName("lblUsuarioSesion")
        self.lblPasswordSesion = QtWidgets.QLabel(self.gbSesion)
        self.lblPasswordSesion.setGeometry(QtCore.QRect(20, 80, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblPasswordSesion.setFont(font)
        self.lblPasswordSesion.setObjectName("lblPasswordSesion")
        self.lblNombreSesion = QtWidgets.QLabel(self.gbSesion)
        self.lblNombreSesion.setGeometry(QtCore.QRect(20, 130, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombreSesion.setFont(font)
        self.lblNombreSesion.setObjectName("lblNombreSesion")
        self.lblRoleSesion = QtWidgets.QLabel(self.gbSesion)
        self.lblRoleSesion.setGeometry(QtCore.QRect(20, 180, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblRoleSesion.setFont(font)
        self.lblRoleSesion.setObjectName("lblRoleSesion")

        # Line Edit del nombre de usuario 
        self.leUsuarioSesion = QtWidgets.QLineEdit(self.gbSesion)
        self.leUsuarioSesion.setGeometry(QtCore.QRect(180, 30, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leUsuarioSesion.setFont(font)
        self.leUsuarioSesion.setToolTip("")
        self.leUsuarioSesion.setMaxLength(50)
        self.leUsuarioSesion.setAlignment(QtCore.Qt.AlignCenter)
        self.leUsuarioSesion.setObjectName("leUsuarioSesion")
        """
        #Establece la funcion para cuando se presione enter en el leUsuarioSesion
        self.leUsuarioSesion.returnPressed.connect(self.fnProcesarEnter)
        self.leUsuarioSesion.keyPressEvent = self.keyPressEvent
        """
        # Line Edit del Password 
        self.lePasswordSesion = QtWidgets.QLineEdit(self.gbSesion)
        self.lePasswordSesion.setGeometry(QtCore.QRect(180, 80, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lePasswordSesion.setFont(font)
        self.lePasswordSesion.setToolTip("")
        self.lePasswordSesion.setToolTipDuration(-1)
        self.lePasswordSesion.setMaxLength(50)
        self.lePasswordSesion.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePasswordSesion.setAlignment(QtCore.Qt.AlignCenter)
        self.lePasswordSesion.setReadOnly(False)
        self.lePasswordSesion.setObjectName("lePasswordSesion")
        """
        #Establece la funcion para cuando se presione enter en el lePassword
        self.lePasswordSesion.returnPressed.connect(self.fnProcesarEnter)

        # Establece la funcion procesar cambio de texto en el password
        self.lePasswordSesion.textChanged.connect(self.fnProcesarCambioTexto)

        """

        # Line Edit para capturar el Role del usuario
        self.leRoleSesion = QtWidgets.QLineEdit(self.gbSesion)
        self.leRoleSesion.setGeometry(QtCore.QRect(180, 180, 221, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.leRoleSesion.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leRoleSesion.setFont(font)
        self.leRoleSesion.setMaxLength(10)
        self.leRoleSesion.setAlignment(QtCore.Qt.AlignCenter)
        self.leRoleSesion.setReadOnly(True)
        self.leRoleSesion.setObjectName("leRoleSesion")
        self.leNombreSesion = QtWidgets.QLineEdit(self.gbSesion)
        self.leNombreSesion.setGeometry(QtCore.QRect(180, 130, 220, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.leNombreSesion.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.leNombreSesion.setFont(font)
        self.leNombreSesion.setAlignment(QtCore.Qt.AlignCenter)
        self.leNombreSesion.setReadOnly(True)
        self.leNombreSesion.setObjectName("leNombreSesion")
       
        self.pbAceptarSesion = QtWidgets.QPushButton(dlgSesion)
        self.pbAceptarSesion.setGeometry(QtCore.QRect(240, 260, 180, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/aceptar2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbAceptarSesion.setIcon(icon)
        self.pbAceptarSesion.setIconSize(QtCore.QSize(50, 50))
        self.pbAceptarSesion.setObjectName("pbAceptarSesion")
        self.pbCancelarSesion = QtWidgets.QPushButton(dlgSesion)
        self.pbCancelarSesion.setGeometry(QtCore.QRect(10, 260, 180, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/icons8-cancelar-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbCancelarSesion.setIcon(icon1)
        self.pbCancelarSesion.setIconSize(QtCore.QSize(32, 32))
        self.pbCancelarSesion.setObjectName("pbCancelarSesion")

        self.retranslateUi(dlgSesion)
        QtCore.QMetaObject.connectSlotsByName(dlgSesion)
        dlgSesion.setTabOrder(self.leUsuarioSesion, self.lePasswordSesion)
        dlgSesion.setTabOrder(self.lePasswordSesion, self.pbAceptarSesion)
        dlgSesion.setTabOrder(self.pbAceptarSesion, self.pbCancelarSesion)
        dlgSesion.setTabOrder(self.pbCancelarSesion, self.leNombreSesion)
        dlgSesion.setTabOrder(self.leNombreSesion, self.leRoleSesion)

    def retranslateUi(self, dlgSesion):
        _translate = QtCore.QCoreApplication.translate
        dlgSesion.setWindowTitle(_translate("dlgSesion", "Inicio de Sesión"))
        self.gbSesion.setTitle(_translate("dlgSesion", "Capture su Usuario y Password"))
        self.lblUsuarioSesion.setText(_translate("dlgSesion", "Usuario:"))
        self.lblPasswordSesion.setText(_translate("dlgSesion", "Password:"))
        self.lblNombreSesion.setText(_translate("dlgSesion", "Nombre:"))
        self.lblRoleSesion.setText(_translate("dlgSesion", "Role:"))
        self.leUsuarioSesion.setText(_translate("dlgSesion", "mi usuario"))
        self.leRoleSesion.setText(_translate("dlgSesion", "Unknow"))
        self.leNombreSesion.setText(_translate("dlgSesion", "Unknow"))
        self.lePasswordSesion.setText(_translate("dlgSesion", "Unknow"))
        self.pbAceptarSesion.setText(_translate("dlgSesion", "Aceptar"))
        self.pbCancelarSesion.setText(_translate("dlgSesion", "Cancelar"))

    """
    def fnProcesarEnter(self):
        print("has presionado ENTER")

        #Se verifica si tiene el foco el usuario 
        if(self.leUsuarioSesion.hasFocus()):
            # manda el foco al pasword
            print("foco al Password")
            self.lePasswordSesion.setFocus()
        else:
            #El foco lo tiene el password
            print("El foco a Aceptar")
            self.pbAceptarSesion.setFocus()

    # Funcion para detectar cambios
    def fnProcesarCambioTexto(self):
        #Verifica si tiene el foco el usuario
        if(self.leUsuarioSesion.hasFocus()):
            # manda el focus al password
            print("Cambio de texto en usuario")
            print(self.leUsuarioSesion.text())
        else:
            #El foco lo tiene el password
            print("Cambio de Texto en Password")
            print(self.lePasswordSesion.text())

    # Se ha presionado una tecla 
    def keyPressEvent(self, event):
        print("se ha presionado una tecla: ", event.text())

        # Verifica si tiene el foco el Usuario 
        if(self.leUsuarioSesion.hasFocus()):
            # El Usuario tiene el Foco
            print("Presionaste una tecla en Usuario")

            # Evitando el 5
            if(event.text()!="5"):
                return QtWidgets.QLineEdit.keyPressEvent(self.leUsuarioSesion, event)
        elif(self.lePasswordSesion.hasFocus()):
            # El foco lo tiene el Password
            print("Presionaste una tecla en Password")
    """



