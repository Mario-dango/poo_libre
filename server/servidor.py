#!/usr/bin/python 
# -*- coding: utf-8 -*-

from xmlrpc_server import XmlRpcEjemploServer
from opciones import ObjetoX

if __name__ == "__main__":
    objeto_vinculado = ObjetoX()
    servidor = XmlRpcEjemploServer(objeto_vinculado)
    