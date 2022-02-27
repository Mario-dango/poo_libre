#include<stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;

int main(void){
  int c;
  /* configuramos el terminal para que las pulsaciones se envien
     directamente a stdin */
  system ("/bin/stty raw");
  while((c=getchar())!= '.') {
    /* Tienes que encontrar un mecanismo de escape alternativo a CTRL-D,
       ya que éste no funciona en el modo 'raw' */
    cout << " " << endl;
    putchar(c);
    //cout << c << endl;
  }
  /* Se restaura el modo normal de trabajo de la terminal */
  system ("/bin/stty cooked");
  return 0;
}