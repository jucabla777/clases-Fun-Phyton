"""numero1 = int(input("ingrese numero "))
numero2 = int(input("ingrese otro numero "))

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero1} es menor que {numero2}")
else:
    print("el numero es igual")"""

peso = float(input("ingrese su PESO "))
Altura = float(input("ingrese su ALTURA "))

IMC = peso / (Altura * Altura)

if IMC < 18.5:
    clasificacion = "PESO BAJO"
elif IMC >= 18.5 and IMC <= 24.9:
    clasificacion = "PESO NORMAL"
elif IMC >= 25.0 and IMC <= 29.9:
    clasificacion = "SOBRE PESO"
else:
    clasificacion = "OBESIDAD"

print(f"su IMC es {IMC: .2f}")
print(f"su clasificacion es {clasificacion}")
print("hola")





