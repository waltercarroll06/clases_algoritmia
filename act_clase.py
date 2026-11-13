import json as js
import pickle as pk
class Empleado:

 def __init__(self,nombre,cargo):
  self.nombre = nombre
  self.cargo = cargo

 def detalles(self):
  return {
   "nombre": self.nombre,
   "cargo": self.cargo
  }


while True:
 nombre = input("ingresa tu nombre: ")
 cargo = input("ingresa tu cargo: ")

 if nombre.isdigit():
  print("nombre no puede tener numeros")
  
 elif cargo.isdigit():
  print("cargo no puede tener numeros")
 else:
  print("info completa...")
  break

e1 = Empleado(nombre,cargo)



with open("empleado.pkl","wb") as f: 
 pk.dump(e1.detalles(),f)

with open("empleado.pkl","rb") as f: 
 lectura = pk.load(f)

print(lectura)
 