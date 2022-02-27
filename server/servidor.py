#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from control_ui import Ventana

if __name__ == "__main__":

    #Instancia para iniciar una aplicación
    app = QApplication(sys.argv)
    #Crear un objeto de la clase
    panel_control = Ventana()
    #Mostra la ventana
    panel_control.show()
    #Ejecutar la aplicación
    app.exec_()
    