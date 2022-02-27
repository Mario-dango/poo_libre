/* cliente_basico.cpp : ejemplo sencillo de cliente XMLRPC.
   Se usa la libreria XmlRpc++
   disponible en http://sourceforge.net/projects/xmlrpcpp/
   y documentacion general en http://xmlrpcpp.sourceforge.net/  
*/
#include <iostream>
#include <stdlib.h>
using namespace std;
#include "XmlRpc.h"
using namespace XmlRpc;

int main(int argc, char* argv[])
{
  //Se indica el servidor deseado
  //string ip_host = "127.0.0.1";  
  int port = 8891;
  try{
    XmlRpc::XmlRpcClient c("127.0.0.1", port);
    //XmlRpc::setVerbosity(5);

    XmlRpc::XmlRpcValue sinArgs, unArg, dosArgs, resultado;

    // Se invoca a la función que corresponda
    // segun los argumentos provistos
    if (argc == 2) {
      // Llamada al metodo saludar
      unArg[0] = argv[1];
      if (c.execute("saludar", unArg, resultado))
        std::cout << resultado << "\n\n";
      else
        std::cout << "Error en la llamada a 'saludar'\n\n";

    }
    else if(argc == 3){
      // Llamada al metodo calcular con 2 flotantes
      dosArgs[0] = std::stod(argv[1]);
      dosArgs[1] = std::stod(argv[2]);
      
      // Forma de preparar y enviar información general 
      // sin usar argumentos de linea de comandos
      //dosArgs[2] = this->mirobot.miartic(i).getestado();
      //dosArgs[3] = qt4.button2.getValue();
     
      if (c.execute("calcular", dosArgs, resultado))
          std::cout << resultado << "\n\n";
      else
        std::cout << "Error en la llamada a 'calcular'\n\n";

      if (c.execute("calcularN", dosArgs, resultado)){
          // analisis de tipo de datos devuelto por el servidor
          string tipo_dato = resultado.getType()==1?"BOOLEAN":
              (resultado.getType()==2?"INTEGER":
                  (resultado.getType()==3?"DOUBLE":
                      (resultado.getType()==4?"STRING":"OTRO TIPO")                  
                  )
               );
          std::cout << "Recibido un tipo " << tipo_dato << endl;
          
          // Conversion al tipo de datos deseado a partir de lo recibido
          double val= std::stod(resultado);
          std::cout << "con Valor " << val << endl;
      }
      else
        std::cout << "Error en la llamada a 'calcularN'\n\n";

    }
    else{
      // Llamada al metodo saludar
      if (c.execute("saludar", sinArgs, resultado))
        std::cout << resultado << "\n\n";
      else
        std::cout << "Error en la llamada a 'saludar'\n\n";

      if (c.execute("calcular", sinArgs, resultado))
        std::cout << resultado << "\n\n";
      else
        std::cout << "Error en la llamada a 'calcular'\n\n";
    }
  }catch(XmlRpc::XmlRpcException e){
      cout << "Error numero " << e.getCode() << ", " << e.getMessage() << endl; 
  }
  
  return 0;
}
