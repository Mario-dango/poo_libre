
import sys
from typing import final
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from robot_bt import robot

import serial

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
 #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("control_bt.ui", self)
        self.setWindowTitle("Interfaz de control para Tan-k")
        self.setMinimumSize(1000,600) 
        self.setMaximumSize(1001,701)        
        # setting auto scroll property
        self.r_log.setAutoScroll(True)  
        self.r_log.setAutoScrollMargin(20)
        #Atributos banderas de estados
        self.estado_mt = False
        self.estado_bt = False
        self.estado_sv = False
        self.teclado_ctrl = False
        #Creo al objeto robot tank
        self.tank = robot
        #Colores estado de botoón servidor
        self.btnDesactivo = "background-color: red; border: 1px; padding: 10px"
        self.btnActivo = "background-color: green; border: 1px; padding: 10px"
        #Botones para habilitar o deshabilitar parametros
        self.on_off_motor.clicked.connect(self.en_motors)
        self.on_off_bt.setCheckable(True)
        self.on_off_bt.toggle()
        self.on_off_bt.clicked.connect(self.conn_bt)
        self.on_off_server.setCheckable(True)
        self.on_off_server.toggle()
        self.on_off_server.clicked.connect(self.en_sv)
        #Botones de control para el movimiento del robot
        self.btn_avanzar.clicked.connect(self.adelante)
        self.btn_retroceder.clicked.connect(self.retrocede)
        self.btn_izquierda.clicked.connect(self.izquierda)
        self.btn_derecha.clicked.connect(self.derecha)
        self.btn_detener.clicked.connect(self.detener)

    #Evento para cuando la ventana se muestra60
    def showEvent(self, event):
        self.autor.setText("Autor: Mario Papetti Funes \nInstagram: Mario.dango")
        self.label_2.setText("Registro de acciones realizadas:")
        self.t_botones.setText("Botones para controlar el movimiento del robot.")
        if self.estado_bt is False:
            self.on_off_motor.setEnabled(False)
            self.btn_avanzar.setEnabled(False)
            self.btn_retroceder.setEnabled(False)
            self.btn_izquierda.setEnabled(False)
            self.btn_derecha.setEnabled(False)
            self.btn_detener.setEnabled(False)
        self.r_log.addItem("Bienvenido a la interfaz para controlar al robot TANK")
        self.r_log.addItem("Para habilitar los botones de control para su movimiento debe de conectar primero el respectivo dispositivo Bluetooth del robot")
        #Eventos para conexión/desconexión activación y desactivación de parametros
    def conn_bt(self):
        bt_device = self.bt_list.currentText()
        if self.estado_bt is False:
            try: 
                self.port_bt = serial.Serial('/dev/rfcomm0',9600)
                self.r_log.addItem("Se logró la conexión con el dispositivo: " + bt_device)
                self.on_off_bt.setText("Bluetooth Conectado!")
                self.on_off_motor.setEnabled(True)
                self.btn_avanzar.setEnabled(True)
                self.btn_retroceder.setEnabled(True)
                self.btn_izquierda.setEnabled(True)
                self.btn_derecha.setEnabled(True)
                self.btn_detener.setEnabled(True)
                self.estado_bt = True
            except:
                self.r_log.addItem("Se produjo un error al intentar abrir comunicación por el puerto rfcomm0.")
                self.r_log.addItem("Favor de revisar la conexión al dispositivo bluetooth.")
                self.on_off_bt.setText("Puerto BT no encontrado")


        else:
            self.estado_bt = False
            self.on_off_motor.setEnabled(False)
            self.btn_avanzar.setEnabled(False)
            self.btn_retroceder.setEnabled(False)
            self.btn_izquierda.setEnabled(False)
            self.btn_derecha.setEnabled(False)
            self.btn_detener.setEnabled(False)
            self.r_log.addItem("Se desconectó del dispositivo: " + bt_device)
            self.on_off_bt.setText("Bluetooth Desconectado")
        self.r_log.addItem(" ")
        self.r_log.addItem("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        self.r_log.scrollToBottom()


    def en_sv(self):
        if self.estado_sv is False:
            self.estado_sv = True
            self.r_log.addItem("Conectado al servidor")
            print("Conectado al servidor")
            self.on_off_server.setText("Servidor: Iniciado!")
            self.on_off_server.setStyleSheet(self.btnActivo)
    
        else:
            self.estado_sv = False
            self.r_log.addItem("Desconectado del Servidor")
            print("Desconectado del Servidor")
            self.on_off_server.setText("Servidor: Finalizado!")
            self.on_off_server.setStyleSheet(self.btnDesactivo)
        self.r_log.addItem("##############################################")
        self.r_log.scrollToBottom()


    ############################################################
    #Evento para inicializar/finalizar la comunicación Bluetooth
    def en_motors(self):
        if self.estado_mt is False:
            self.estado_mt = True
            self.teclado_ctrl = True
            self.tank.on_motor(self, self.port_bt)
            self.r_log.addItem("Motores activados.")
        else:
            self.estado_mt = False
            self.tank.off_motor(self, self.port_bt)
            self.r_log.addItem("Motores desactivados.")
        self.r_log.addItem("##############################################")
        self.r_log.scrollToBottom()

        ###################################################
        #Eventos de botones para control de los movimientos
    def adelante(self):
        self.r_log.addItem("Se presionó el botón para avanzar.")
        print("Se presionó el botón para avanzar.")
        try:            
            self.tank.avanzar(self, self.port_bt)

        except:
            self.r_log.addItem("Error al intentar enviar comando Avanzar.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
        finally:
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
    
    def retrocede(self):
        self.r_log.addItem("Se presionó el botón para retroceder.")
        print("Se presionó el botón para retroceder.")
        try:            
            self.tank.retroceder(self, self.port_bt)

        except:
            self.r_log.addItem("Error al intentar enviar comando retroceder.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
        finally:
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
        
    def izquierda(self):
        self.r_log.addItem("Se presionó el botón para izquierda.")
        print("Se presionó el botón para girar a la izquierda.")
        try:            
            self.tank.izquierda(self, self.port_bt)

        except:
            self.r_log.addItem("Error al intentar enviar comando izquierda.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
        finally:
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
        
    def derecha(self):
        self.r_log.addItem("Se presionó el botón para derecha.")
        print("Se presionó el botón para girar a la derecha.")
        try:            
            self.tank.derecha(self, self.port_bt)

        except:
            self.r_log.addItem("Error al intentar enviar comando derecha.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
        finally:
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
        
    def detener(self):
        self.r_log.addItem("Se presionó el botón para detener.")
        print("Se presionó el botón para detener.")
        
        try:            
            self.tank.detener(self, self.port_bt)

        except:
            self.r_log.addItem("Error al intentar enviar comando detener.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
        finally:
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()

    #Eventos para controlar los movimientos del robot con le pad númerico del teclado
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_8 and self.teclado_ctrl == True:
            self.adelante()
        elif event.key() == Qt.Key_2 and self.teclado_ctrl == True:
            self.retrocede()
        elif event.key() == Qt.Key_4 and self.teclado_ctrl == True:
            self.izquierda()
        elif event.key() == Qt.Key_6 and self.teclado_ctrl == True:
            self.derecha()
        elif event.key() == Qt.Key_5 and self.teclado_ctrl == True:
            self.detener()

  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()