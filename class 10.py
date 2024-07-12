"""class Car:

    def __init__(self, marca, modelo, VelMax, Precio):
        self.marca=marca
        self.modelo=modelo
        self.__VelMax=VelMax
        self.__Precio=Precio

    
    def acelerar(self):
        print(self.__VelMax+(10))
    def precio(self):
        print(self.__Precio+(self.__Precio*.10))
    def mod(self):
        print("el modelo de este campero es", self.modelo, "y la marca", self.marca)
   


automovil_1=Car("zotye", "nomada", 120, 30000000)
automvil

automovil_1.acelerar()
automovil_1.precio()
automovil_1.mod()"""


"""class Calculadora:
    def __init__(self, numero):
        self.resultado=numero
    
    def suma(self, numero):
        self.resultado+=numero
    
    def resta(self, numero):
        self.resultado-=numero

    def multiplicacion(self, numero):
        self.resultado*=numero

    def dividir(self, numero):
        if numero != 0:
            self.resultado/=numero
        else:
           print("error no se permite division por 0")
        
    def obt_resultado(self):
        return self.resultado


calculo=Calculadora(0)



calculo.suma(10)
calculo.resta(2)
calculo.multiplicacion(4)
calculo.dividir(2)

resultado_op=calculo.obt_resultado()
print(resultado_op)"""


class Calculadora2:
    def suma(self, numero1, numero2):
        return numero1+numero2
    
    def resta(self, numero1, numero2):
        return numero1-numero2

    def multiplicacion(self, numero1, numero2):
        return numero1*numero2

    def dividir(self, numero1, numero2):
        if numero2==0:
            print("imposible dividir por 0")
        else:
            return numero1/numero2

calculadora=Calculadora2()           

numero1 = float(input("ingrese primer valor "))
numero2 = float(input("ingrese segundo valor "))


print(calculadora.suma(numero1, numero2))
print(calculadora.resta(numero1, numero2))
print(calculadora.multiplicacion(numero1, numero2))
print(calculadora.dividir(numero1, numero2))















        
   

    
        


    