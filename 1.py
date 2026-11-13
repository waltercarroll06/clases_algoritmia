
class Persona:
 
 def __init__(self,nombre,edad): 
  self.nombre = nombre 
  self.edad = edad

 def guardar_archivo(self):
    with open ("inventario.txt", "a" ) as archivo:
        archivo.write(f"{self.nombre},{self.edad}\n")
        
 def leer_archivo(self):
   with open("inventario.txt", "r") as t:
     return [(l.strip()) for l in t if l.strip()]



   
p1 = Persona("walter",20)
p1.guardar_archivo()
p1.leer_archivo()



 