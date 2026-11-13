import pickle as pk
import json as js
objeto = {
 "nombre": "walter",
 "edad": 23
}
with open ("objeto.pkl", "wb") as f:
    pk.dump(objeto,f)

with open("Objeto.pkl","rb") as f:
    lectura = pk.load(f)

print(lectura)


class Persona:

    def __init__(self,nombre,edad,ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def detalles(self):
        return {"nombre": self.nombre,
                "edad": self.edad,
                "ciudad" : self.ciudad}


p1 = Persona("walter",20,"cali")

with open("prueba_act_cl3","wb") as f:
    pk.dump(p1.detalles(),f)

with open("prueba_act_cl3","rb") as f:
    lectura = pk.load(f)


print(lectura)


p2 = Persona("juan",39,"cali")
with open("dicionario_json.json", "w") as f:
    js.dump(p2.detalles(),f)

with open("dicionario_json.json", "r") as f:
    lectura = js.load(f)

print(lectura)
