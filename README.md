# poo_libre
Proyecto de caracter libre para la asignatura de Programación Orientada a Objetos (POO) de la UNCuyo.

El mismo consta de la creación de una interfaz capaz de comunicarse con el Robot mediante Bluetooth funcionando cómo control remoto, dicha interfaz ha sido diseñada con PyQT5 y se le agregó la funcionalidad de poder activar una comunicación servidor-cliente mediante protocolo XML-RPC, donde el cliente que se conectará también poseerá una interfaz gráfica con la sutil diferencia que tanto la interfaz cómo toda la parte encargada del cliente es escrita en C++ mientras en el servidor es netamente Python, sin contar el Robot que posee C++.
