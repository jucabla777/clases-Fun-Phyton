# las funciones son bloques de codigo que son reutilizables solo hay que crear la funcion y luego invocarla
# funcion "def" ejemplo creamos una funcion para que imprima "hola" con def al ejecutar solo es poner dihola() y se ejecuta 
#en el parentesis van os parametros si los necesitara la funcion
#scope es la propiedad de la funcion de usar las variables fuera del bloque y dentro del bloque... pero lo de fuera no puede usar lo de la funcion

"""def dihola(): 
    print("hola")

dihola()

def sumar_3_numeros(a,b,c):
    #print(a+b+c) modo simple
    resultado=a+b+c
    print(resultado)

sumar_3_numeros(1,2,3)
sumar_3_numeros(10,23,45)"""

#"return" "regresar funcion" sirve para guardar el resultado de una funcion en una variable y termina el bloque de "def"

"""def sumar_3_numeros(a,b,c):
    resultado=a+b+c
    #print(resultado)
    return resultado

x=sumar_3_numeros(2,4,6)
print(x)"""

"""while" "mientras" a diferencia de "for" ejecuta un bucle indefinidamente de interaciones cuando se cumple una condicion 
(condicion true) for ejecuta un bucle de forma determinada de interaciones (las veces que se defina en el codigo)"""

"""numero=int(input("digite un numero: "))"""

"""while numero <= 0:
    print("ERROR...DEBE SER POSITIVO")
    numero=int(input("digite un numero: "))
print(numero * 10)"""

"""x = 2
while x<10:
    print(x)
    x += 1"""

"""numero=int(input("digite un numero: "))

suma = 0

while numero != 0:
    suma = suma + numero
    print ("ingrese otro numero menor")
    numero=int(input("digite un numero: "))
    
print("el total es :", suma)"""



"""def multiplicar(n,):
    print(n*1000)

multiplicar(20)

lista = [1,2,3,4,5]

def maximo(lista):
    print(max(lista))

maximo(lista)


lista = ["mono", "perro", "gato"]

lista.append("raton")

print(lista)

lista.sort()

print(lista)"""


lista2 = [3, -1, -7, 2, 5]

def agregar(lista2):
    lista2.append(10)
    print(lista2)

agregar(lista2)

def quitar(lista2):
    lista2.remove(5)
    print(lista2)

quitar(lista2)


def ordenar(lista2):
    lista2.sort()
    print(lista2)

ordenar(lista2)

def invertir(lista2):
    lista2.reverse()
    print(lista2)

invertir(lista2)






















