/* cliente_basico.cpp : ejemplo sencillo de cliente XMLRPC.
   Se usa la libreria XmlRpc++
   disponible en http://sourceforge.net/projects/xmlrpcpp/
   y documentacion general en http://xmlrpcpp.sourceforge.net/  
*/
// ejemplo de compilación que funciona
//g++ -Wall cliente_basico.cpp XmlRpcClient.cpp XmlRpcUtil.cpp XmlRpcValue.cpp XmlRpcSocket.cpp XmlRpcSource.cpp XmlRpcDispatch.cpp -o cliente
//funciona para compilar~~~~~~~

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
#include "XmlRpc.h"
using namespace XmlRpc;

int main(int argc, char* argv[])
{
  //Se indica el servidor deseado
  //string ip_host = "127.0.0.1";  
  int port = 8891;
  int letra = 0;

  try{
    XmlRpc::XmlRpcClient cliente("127.0.0.1", port);
    //XmlRpc::setVerbosity(5);

    XmlRpc::XmlRpcValue vacio, tecla, resultado;

    while (true){
      char tecla;
      system ("/bin/stty raw"); 
      std::cout << "Por favor ingresar valores númericos correspondinte a los movimientos" << endl;
      while ((tecla=getchar()) != 'q')
      {
        printf("Se ha presionado: %c\n", tecla);
        if (tecla == 'y'){
          if (cliente.execute("avanzar", vacio, resultado)){
            std::cout << resultado << "\n";
          }else{
            std::cout << "Error en la llamada avanzar!" << "\n";
          }
        }else if (tecla == 'h'){
          if (cliente.execute("retroceder", vacio, resultado)){
            std::cout << resultado << "\n";
          }else{
            std::cout << "Error en la llamada Retroceder!" << "\n";
          }
        }else if (tecla == 'g'){
          if (cliente.execute("izquierda", vacio, resultado)){
            std::cout << resultado << "\n";
          }else{
            std::cout << "Error en la llamada Izquierda!" << "\n";
          }
        }else if (tecla == 'j'){
          if (cliente.execute("derecha", vacio, resultado)){
            std::cout << resultado << "\n";
          }else{
            std::cout << "Error en la llamada Derecha!" << "\n";
          }
        }else if (tecla == 'u'){
          if (cliente.execute("detenerse", vacio, resultado)){
            std::cout << resultado << "\n";
          }else{
            std::cout << "Error en la llamada Detener!" << "\n";
          }
        }else if (tecla == 't'){
          std::cout << "se procede a salir de la conexión." << "\n\n";
          break;
        }       
      }
      system ("/bin/stty cooked");
      return 0;
    }
  }catch(XmlRpc::XmlRpcException e){
      cout << "Error numero " << e.getCode() << ", " << e.getMessage() << endl; 
  }  
  return 0;
}