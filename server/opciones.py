class ObjetoX:
    
    def saludar(self, quien):
        return "Hola " + str(quien)

    def calcular(self, num1, num2):
        res = str(float(num1)+float(num2))
        print("Recibidos " + str(num1) \
    + " y " + str(num2) + ". Se obtiene " + res)
        return "Resultado de " + str(num1) \
    + "+" + str(num2) + " = " + res

    def calcularN(self, num1, num2):
        res = str(float(num1)+float(num2))
        return res
