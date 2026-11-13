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

e1 = Empleado("walter","gerente")

with open("empleado.pkl","wb") as f 
   
 