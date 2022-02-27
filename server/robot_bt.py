class robot():
    
    def avanzar(self, bt):
        try:
            bt.write(b'8')
        except:
            return "error en comunicación"
    
    def retroceder(self, bt):
        try:
            bt.write(b'2')
        except:
            return "error en comunicación"
    
    def derecha(self, bt):
        try:
            bt.write(b'6')
        except:
            return "error en comunicación"
    
    def izquierda(self, bt):
        try:
            bt.write(b'4')
        except:
            return "error en comunicación"
    
    def detener(self, bt):
        try:
            bt.write(b'0')
        except:
            return "error en comunicación"
    
    def on_motor(self, bt):
        try:
            return bt.write(b'A')
        except:
            return "error en comunicación"
    
    def off_motor(self, bt):
        try:
            return bt.write(b'B')
        except:
            return "error en comunicación"
    
    def avanzar(self, bt):
        try:
            bt.write(b'8')
        except:
            return "error"

    def saludar(self, quien):
        return "Hola " + str(quien)