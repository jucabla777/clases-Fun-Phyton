# PROGRAMACION ORIENTADA A OBJETOS y CLASES

class Dog:
    especie="canine"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrido(self):
        print(f"{self.nombre}, dice gua gua")
    
    def descripcion(self):
        return self.nombre
    
    def sumar_edad(self):
        print("la edad del perros es", 
              self.edad+1)


perro1 = Dog("tony", 3)
perro2 = Dog("firulay", 5)

print(perro1.especie, perro1.nombre, perro1.edad)
print(perro2.especie, perro2.nombre, perro2.edad)

perro1.ladrido()

perro1.sumar_edad()
perro2.sumar_edad()

print(perro1.descripcion())










