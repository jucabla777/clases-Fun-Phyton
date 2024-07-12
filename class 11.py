#herencia y poliformismo

class Dispositivo_electronico: # CLASE PADRE
    def __init__(self, marca, modelo, capacidad):
        self.marca=marca
        self.modelo=modelo
        self.capacidad=capacidad

    def encender(self):
        return f"{self.marca} {self.modelo} disposivo encendido"
    
class Telefono(Dispositivo_electronico): #clase HIJA
    
    def hacer_llamada(self, num):
        return f"esta llamando al telefono {num}"
    
class Portatil(Dispositivo_electronico):

    def abrir_programa(self, programa):
        return f"abriendo {programa}"

telefono=Telefono("nokia", "2900", "2 gigas")
portatil=Portatil("Dell", "latitud", "4 gigas")

print(f"el telefono es {telefono.marca} modelo {telefono.modelo}") # herencia
print(f"el portatil es {portatil.marca} modelo {portatil.modelo}")

print(telefono.hacer_llamada(3146267147))
print(portatil.abrir_programa("excel"))

print(telefono.encender())  #poliformismo
print(portatil.encender())
print(telefono)


#
    



    
    







    


        
        
