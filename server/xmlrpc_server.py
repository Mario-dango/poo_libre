#!/usr/bin/python 
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import socket

class XmlRpc_servidor(object):
    server = None
    RPC_PORT = 8891
    estado_sv = False

    def __init__(self, interfaz, port = RPC_PORT):
        self.puerto_usado = port
        self.interfaz = interfaz
        while True:
            try:
                #Creacion del servidor indicando el puerto deseado
                self.server = SimpleXMLRPCServer(("localhost", self.puerto_usado), allow_none = True, logRequests = False)
                if self.puerto_usado != port:
                    print("Servidor RPC ubicado en puerto no estándar [%d]" % self.puerto_usado)
                break
            except socket.error as e:
                if e.errno == 98:
                    self.puerto_usado += 1
                    continue
                else:
                    print("El servidor RPC no puede ser iniciado")
                    raise

        #Se registra cada funcion
        self.server.register_function(self.do_escribir, 'escribir')
        self.server.register_function(self.do_on_off_bt,'buetooth')
        self.server.register_function(self.do_on_off_mt,'motores')
        self.server.register_function(self.do_avanzar,'avanzar')
        self.server.register_function(self.do_retroceder,'retroceder')
        self.server.register_function(self.do_derecha,'derecha')
        self.server.register_function(self.do_izquierda,'izquierda')
        self.server.register_function(self.do_detenerse,'detenerse')
        
        #Se lanza el servidor
        self.thread = Thread(target = self.run_server)
        self.thread.start()
        print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))

    def run_server(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
        self.thread.join()

    def do_escribir(self, texto):
        # Funcion/servicio: mensaje al argumento provisto
        return self.interfaz.escribir(texto)
    
    def do_on_off_bt(self, estado_bt):
        if estado_bt is True:
            return self.interfaz.conn_bt()
        elif estado_bt is False:
            return "Bluetooth desactivado."
    def do_on_off_mt(self):
        return self.interfaz.en_motors()
    def do_avanzar(self):
        return self.interfaz.adelante()
    def do_retroceder(self):
        return self.interfaz.retrocede()
    def do_derecha(self):
        return self.interfaz.izquierda()
    def do_izquierda(self):
        return self.interfaz.derecha()
    def do_detenerse(self):
        return self.interfaz.detener()


