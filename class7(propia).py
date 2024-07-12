def mostrar_menu():
    print("calculadora Basica digita la operacion a realizar:")
    print("1 para sumar +")
    print("2 para restar -")
    print("3 para multiplicar *")
    print("4 para dividir /")
    print("5 para salir")


def sumar(numero1, numero2):
    return numero1+numero2

def restar(numero1, numero2):
    return numero1-numero2

def multiplicar(numero1, numero2):
    return numero1*numero2   

def dividir(numero1, numero2):
    return numero1/numero2

"""def calculadora():
    while True:
        mostrar_menu()
        operacion = int(input("ingrese operacion deseada "))
        
        if operacion == 5:
            print("abandona calculadora chao.....")
            break

        if operacion in [1,2,3,4,]:
        
            a=int(input("digite un numero: "))
            b=int(input("digite un numero: "))
            if operacion == 1:
                print("elresultado es: ", sumar(a,b))
            elif operacion == 2:
                print("elresultado es: ", restar(a,b))
            elif operacion == 3:
                print("elresultado es: ", multiplicar(a,b))
            elif operacion == 4:
                print("elresultado es: ", dividir(a,b))
        else:
            print("operacion no valida")
 
 
calculadora()"""

def calculadora2():
    while True:
        mostrar_menu()
        
        operacion=input("operacion deseada: ")
        
        if operacion == "5":
            print("saliendo chao....")
            break
            
        numero1=float(input("digite un numero: "))
        numero2=float(input("digite un numero: "))

        if operacion == "+":
            print(numero1+numero2)
        elif operacion == "-":
            print(numero1-numero2)
        elif operacion == "*":
            print(numero1*numero2)
        elif operacion == "/":
            print(numero1/numero2)   
        else:
            print("operacion no valida")

calculadora2()








        

        






























