import os

def crear_archivo():
    lista = []

    bandera = 0
    while bandera < 3:
       nombre = input("nombre: ")
       lista.append(nombre)
       bandera += 1

    with open ("estudiantes.txt", "w") as archivo:
        for i in lista:
            archivo.write(i + "\n")






def leer_contar():
   with open ("estudiantes.txt","r") as t:
      registros = len(t.readlines())
      for n in t:
         print(n)
      return f"total de registros : {registros}"
   
def comprobar_archivo():
 while True:

   nombre_archivo = input("Ingrese el nombre del archivo: ").strip()

   if os.path.isfile(nombre_archivo):
      print("archivo existe")
      while True:
        opcion = int(input("si desea leer el archivo presione 1, si no presione 2: "))
        if opcion == 1:
           print(leer_contar())
           break
        elif opcion == 2:
           break
        else:
           print("numero incorrecto")
      break
   else:
      print("archivo no existe, intentelo de nuevo")
  
def agregar_registros():
 comprobar_archivo()
 nuevo_nombre_1 = input("nombre: ")
 nuevo_nombre_2 = input("nombre: ")
 return nuevo_nombre_1, nuevo_nombre_2



def agregar_registro_archivo(x , y):
   with open ("estudiantes.text", "a") as t: 
      t.write(f"{x}\n{y}")


crear_archivo()
x , y = agregar_registros()
agregar_registro_archivo(x , y)

comprobar_archivo()

   


    
