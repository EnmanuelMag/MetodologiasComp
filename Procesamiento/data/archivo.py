import funciones as fn
import os

rutaParcial = "../detalle/"
dicc = {}

print("Cargando y limpiando comentarios. . .")
for nombreArchivo in os.listdir(rutaParcial):

    rutaCompleta = os.path.join(rutaParcial, nombreArchivo)
    archivo = open(rutaCompleta, "r", encoding='UTF8')
    nombreArchivo = nombreArchivo.replace(".txt", "")

    indTermino = nombreArchivo.find("1S") if nombreArchivo.find("1S") != -1 else nombreArchivo.find("2S")

    termino = nombreArchivo[indTermino::]
    anio = nombreArchivo[indTermino-4:indTermino]
    codigoMat = nombreArchivo[:indTermino-4]

    profesor = archivo.readline().replace(",", " ").replace("\n", "")

    if anio == "2018":
        # Comentario
        # Linea para salta los especios para llegar al primer comentario
        archivo.readline()
        archivo.readline()

        comentarios = archivo.readlines()
        comentsLimpios = []

        for comentario in comentarios:

            if len(comentario) > 1:
                # 1.Filto las Stopwords
                comentFiltrado = fn.limpiarStopWords(comentario)
                # 2.Sepracion de palabras
                comentsLimpios.append(fn.separarPalabras(comentFiltrado))

        dicc = fn.llenarDiccionario(profesor, codigoMat, termino, anio, comentsLimpios, dicc)

print("ROCÍO ELIZABETH MERA SUÁREZ: " +str(dicc.get("ROCÍO ELIZABETH MERA SUÁREZ")))

#Tambien se puede simplicar palabras como muuuuy a muy
#sin embargo creo que esto si es significativo para nuestro estudio