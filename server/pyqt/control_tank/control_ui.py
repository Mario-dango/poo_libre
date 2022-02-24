import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
 #Método constructor de la clase
    def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("control_bt.ui", self)
        self.setWindowTitle("Interfaz de control para Tan-k")
        self.setMinimumSize(1000,500)
        resolucion = QApplication.desktop()
        resolucion_ancho = resolucion.height() 
        resolucion_alto = resolucion.width()
        vertical =(resolucion_ancho - self.frameSize().width())/2
        horizontal =(resolucion_alto - self.frameSize().height())/2
        self.move(vertical, horizontal)

    #Evento para cuando la ventana se muestra
    def showEvent(self, event):
        self.autor.setText("Autor: Mario Papetti Funes \nInstagram: Mario.dango")

         #Evento para cuando la ventana se cierra
    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir ...", "¿Seguro que quieres salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: event.accept()
        else: event.ignore()
  
  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)
#Crear un objeto de la clase
_ventana = Ventana()
#Mostra la ventana
_ventana.show()
#Ejecutar la aplicación
app.exec_()