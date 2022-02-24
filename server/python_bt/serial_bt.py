"""
    El programa funciona 23/02/2022
    se debe de conectar el bluetooth de la pc antes
    En linux:
        # para prenderlo: bluetoothctl power on      
        # para ver conexioneas: sudo rfkill list
        # para conectar con HC-06 con MAC: sudo rfcomm connect hci 98:D3:31:FC:96:5F
        # una vez conectado, correr el programa: sudo python3 serial_bt.py

    #llega por lo menos hasta unos 28m y máximo unos 48
"""
import serial
import keyboard as teclado

try:
    ser = serial.Serial('/dev/rfcomm0',9600)
    
    while 1==1:
        if teclado.is_pressed("8"):
            #Comando referencia en la app:  8
            print("comando de avance")
            ser.write(b'8')

        elif teclado.is_pressed("2"):
            #Comando referencia en la app:  2
            print("comando de retroceso")
            ser.write(b'2')
            
        elif teclado.is_pressed("0"):
            #Comando referencia en la app:  0
            print("comando de retroceso")
            ser.write(b'0')
            
        elif teclado.is_pressed("4"):
            #Comando referencia en la app:  4
            print("comando de giro derecho")
            ser.write(b'4')
            
        elif teclado.is_pressed("6"):
            #Comando referencia en la app:  6
            print("comando de giro izquierdo")
            ser.write(b'6')
            
        elif teclado.is_pressed("b"):
            #Comando referencia en la app:  B
            print("comando de apagado")
            ser.write(b'B')
            
        elif teclado.is_pressed("a"):
            #Comando referencia en la app:  A
            print("comando de encendido")
            ser.write(b'A')
            
        if teclado.is_pressed(" "):
            print("comando de desconexión")
            ser.write(b'B')
            ser.close()
            break


except:
    print("ERROR!")

finally:
    print("Terminó programa.")            
            
