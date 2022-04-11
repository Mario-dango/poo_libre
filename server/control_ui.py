from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from xmlrpc_server import XmlRpc_servidor

from robot_bt import robot
import serial


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
 #Método constructor de la clase
    def __init__(self):
        #Creo al objeto robot tank
        self.tank = robot
        #dejamos vació al atributo server
        self.xmlrpc_sv = None
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("panel-control.ui", self)
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
        self.r_log.addItem("°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°")
        self.r_log.addItem("Bienvenido a la interfaz para controlar al robot TANK")
        self.r_log.addItem("Para habilitar los botones de control para su movimiento debe de conectar primero el respectivo dispositivo Bluetooth del robot")
        self.r_log.addItem("°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°")
        self.r_log.addItem(" ")
    
    
    #Evento para cuando la ventana se cierra
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:  
            self.estado_bt = False
            if self.estado_mt is True:
                try: 
                    self.en_motors(self)
                except:
                    self.estado_mt = False
            elif self.estado_sv is True:
                try: 
                    self.xmlrpc_sv.shutdown()
                except:
                    self.estado_sv = False  
            else:
                self.estado_bt = False
                self.estado_mt = False
                self.estado_sv = False
                self.xmlrpc_sv = None    
            event.accept()            
        else: 
            event.ignore()
    
    
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
                self.r_log.addItem(" ")
                self.r_log.addItem("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                self.r_log.scrollToBottom()
                return "Se logró establecer la conexión Bluetooth."
            except:
                self.r_log.addItem("Se produjo un error al intentar abrir comunicación por el puerto rfcomm0.")
                self.r_log.addItem("Favor de revisar la conexión al dispositivo bluetooth.")
                self.on_off_bt.setText("Puerto BT no encontrado")
                self.r_log.addItem(" ")
                self.r_log.addItem("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                self.r_log.scrollToBottom()
                return "No se logró establecer la conexión Bluetooth."

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
            return "Se finalizó la conexión Bluetooth."

    #Evento para habilitar o deshabilitar la función de conexión XmlRpc
    def en_sv(self):
        if self.estado_sv is False:
            try:
                #Cero al objeto servidor XmlRpc
                self.xmlrpc_sv = XmlRpc_servidor(self)
                self.estado_sv = True
                self.r_log.addItem("Inicializado el servidor")
                #self.r_log.addItem("Dirección y puerto del servidor: %s" % str(self.xmlrpc_sv.server_address()))
                print("Conectado al servidor")
                self.on_off_server.setText("Servidor: Iniciado!")
                self.on_off_server.setStyleSheet(self.btnActivo)
            except:
                print("Error al intentar inicializar servidor")
                self.r_log.addItem("Error al intentar inicializar servidor")
                
    
        else:
            try:
                self.r_log.addItem("Desconectado del Servidor")
                print("Desconectado del Servidor")
                self.on_off_server.setText("Servidor: Finalizado!")
                #self.r_log.addItem("Dirección y puerto del servidor: %s" % str(self.xmlrpc_sv.server_address()))
                self.on_off_server.setStyleSheet(self.btnDesactivo)
                self.estado_sv = False
                self.xmlrpc_sv.shutdown()
                self.xmlrpc_sv = None
            except:
                print("Error al intentar finalizar servidor")
                self.r_log.addItem("Error al intentar finalizar servidor")
        self.r_log.addItem("##############################################")
        self.r_log.scrollToBottom()


    ############################################################
    #Evento para inicializar/finalizar la comunicación Bluetooth
    def en_motors(self):
        try:
            if self.estado_mt is False:
                self.estado_mt = True
                self.teclado_ctrl = True
                self.tank.on_motor(self, self.port_bt)
                self.r_log.addItem("Motores activados.")
                self.r_log.addItem("##############################################")
                self.r_log.scrollToBottom()
                return "Se han habilitado los motores."
            elif self.estado_mt is True:
                self.estado_mt = False
                self.tank.off_motor(self, self.port_bt)
                self.r_log.addItem("Motores desactivados.")
                self.r_log.addItem("##############################################")
                self.r_log.scrollToBottom()
                return "Se han deshabilitado los motores."
        except:
                self.r_log.addItem("<b>Error!</b> Al intentar activas/desactivar motores.")
                self.r_log.addItem("##############################################")
                self.r_log.scrollToBottom()

        ###################################################
        #Eventos de botones para control de los movimientos
    def adelante(self):
        self.r_log.addItem("Se presionó el botón para AVANZAR.                      ****      ^^      ****")
        print("Se presionó el botón para avanzar.")
        try:            
            self.tank.avanzar(self, self.port_bt)
            self.r_log.scrollToBottom()
            return "El tank se mueve hacia Adelante."

        except:
            self.r_log.addItem("Error al intentar enviar comando Avanzar.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
            return "Error al avanzar."
    
    def retrocede(self):
        self.r_log.addItem("Se presionó el botón para RETROCEDER.              ****         vv         ****")
        print("Se presionó el botón para retroceder.")
        try:            
            self.tank.retroceder(self, self.port_bt)
            self.r_log.scrollToBottom()
            return "El tank se mueve hacia Atras."

        except:
            self.r_log.addItem("Error al intentar enviar comando retroceder.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
            return "Error al retroceder."
        
    def izquierda(self):
        self.r_log.addItem("Se presionó el botón para IZQUIERDA.                ****         <-        ****")
        print("Se presionó el botón para girar a la izquierda.")
        try:            
            self.tank.izquierda(self, self.port_bt)
            self.r_log.scrollToBottom()
            return "El tank comienza a girar hacia la izquierda."

        except:
            self.r_log.addItem("Error al intentar enviar comando izquierda.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
            return "Error al girar a la izquierda."
        
    def derecha(self):
        self.r_log.addItem("Se presionó el botón para DERECHA.                 ****       ->      ****")
        print("Se presionó el botón para girar a la derecha.")
        try:            
            self.tank.derecha(self, self.port_bt)
            self.r_log.scrollToBottom()
            return "El tank comienza a girar hacia la derecha."

        except:
            self.r_log.addItem("Error al intentar enviar comando derecha.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
            return "Error al girar a la derecha."
        
    def detener(self):
        self.r_log.addItem("Se presionó el botón para DETENER.                      ****   [STOPED]   ****")
        print("Se presionó el botón para detener.")
        
        try:            
            self.tank.detener(self, self.port_bt)
            self.r_log.scrollToBottom()
            return "El tank se ha detenido."

        except:
            self.r_log.addItem("Error al intentar enviar comando detener.")
            self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
            self.r_log.addItem(" ")
            self.r_log.scrollToBottom()
            return "Error al Detenerse."

    #Metodo para saludar/recibir mensaje desde Cliente
    def escribir(self, text):
        self.r_log.addItem(text)
        self.r_log.addItem(" ")
        return "Ha llegado su mensaje al Servidor!"

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
