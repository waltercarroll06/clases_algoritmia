class ContadorDePalabras:
    def __init__(self,nombre):
        self.nombre = nombre 


    def  contar_palabras(self):
        with open (self.nombre , "r") as f:
            contenido = f.read()

        lista = contenido.split()
        return f"numero de palabras: {len(lista)}"


a1 = ContadorDePalabras("texto.txt")
a1_palabras = a1.contar_palabras()
print(a1_palabras)





class ConcatenadorDeArchivos:

    def __init__(self,archivos,texto_nuevo):
        self.archivos_lectura = archivos
        self.texto_nuevo = texto_nuevo

    def concatenar(self):
        contenido = ""
        for texto in self.archivos_lectura:
            with open (texto, "r") as f:
               contenido_leido = f.read()
               contenido += contenido_leido + "\n"

        contador = contenido.split()
        total_palabras = len(contador)
        contenido += str(total_palabras)

        with open (self.texto_nuevo,"w") as a: 
            cont = a.write(contenido)
            return cont


a2 = ConcatenadorDeArchivos(["texto.txt","texto2.txt","texto3.txt"], "resultado.txt")
resultado = a2.concatenar()


