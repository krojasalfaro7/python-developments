#!/usr/bin/python3.5

class coche2:
     def __init__(self, gasolina,nombre):
         self.gasolina = gasolina
         self.nombre = nombre
         print("La gasolina del carro es: ", self.gasolina)
     def encender(self):
         if (self.gasolina > 0):
             print("Encendido")
         else:
             print("No hay suficiente gasolina")
     def conducir(self):
         if (self.gasolina > 0):
             self.gasolina -= 1
             print("Conduciendo, queda :", self.gasolina)
         else:
             print("No hay suficiente gasolina")
     def recargar(self,recarga):
         self.gasolina = recarga
         print("La gasolina es: ", self.gasolina)
     def ver_nombre(self):
         print("El nombre del auto es: ", self.nombre)

if __name__ == '__main__':

    print("hello wordl\n")
