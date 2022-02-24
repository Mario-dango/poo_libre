#!/usr/bin/python 
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import socket

class XmlRpcEjemploServer(object):
    server = None
    RPC_PORT = 8891

    def __init__(self, objeto_vinculado, port = RPC_PORT):
        self.objeto_vinculado = objeto_vinculado
        self.puerto_usado = port
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
        self.server.register_function(self.do_saludar, 'saludar')
        self.server.register_function(self.do_calcular,'calcular')
        self.server.register_function(self.do_calcularN,'calcularN')
        
        #Se lanza el servidor
        self.thread = Thread(target = self.run_server)
        self.thread.start()
        print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))

    def run_server(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
        self.thread.join()

    def do_saludar(self, quien='Programador'):
        # Funcion/servicio: mensaje al argumento provisto
        return self.objeto_vinculado.saludar(quien)

    def do_calcular(self, prim=2, seg=5):
        # Funcion/servicio: sumar 2 numeros, devuelve un mensaje
        return self.objeto_vinculado.calcular(prim, seg)

    def do_calcularN(self, prim=2, seg=5):
        # Funcion/servicio: sumar 2 numeros, devuelve un resultado
        return self.objeto_vinculado.calcularN(prim, seg)

