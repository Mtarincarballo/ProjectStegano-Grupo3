# Importamos los módulos necesarios
# Para este proyecto, como se puede ver hemos optado por la utilizacion de opencv
import cv2
import numpy as np
import types

# Esta es la función del menú principal, desde la que llamamos a las opciones mediante su respectiva función
def menu_ppal():

    # El menú consta de un bucle que finalizará cuando se escoja la opción de salir
    while True:

        print()
        print(("\033[1m\033[4mAPLICACIÓN ESTEGANO\033[0m\033[0m".center(100, " ")), end = "\n\n")

        opc_insertada = input("1) Insertar mensaje oculto en una imagen \n2) Extraer mensaje oculto de una imagen \n3) Convertir la imagen a escala de grises \n4) Salir \n\nInserte opción: ")
        opcion = int(opc_insertada)

        if (opcion == 1):
            print("\nOPCIÓN: Insertar mensaje oculto en una imagen\n")
            insertar_msj()

        elif (opcion == 2):
            print("\nOPCIÓN: Extraer mensaje de una imagen\n")
            print("Extrayendo el texto de la imagen...\n\n")
            print("El texto oculto es: " + extraer_msj() + "\n")

        elif (opcion == 3):
            print("\nOPCIÓN: Convertir la imagen a escala de grises\n")
            convertir_a_grises()
            print("\nConvirtiendo la imagen a escala de grises...\n")

        elif (opcion == 4):
            salir()
            break

        else:
            print("\nOpción no admitida, intente de nuevo...\n")

# En esta opción pasamos el mensaje a binario. Será de utilidad en las funciones que ocultan y enseñan el mensaje
def mensaje_a_binario(msj):

    if type(msj) == str:
        return ''.join([format(ord(i), "08b") for i in msj])

    elif type(msj) == bytes or type(msj) == np.ndarray:
        return [format(i, "08b") for i in msj]

    elif type(msj) == int or type(msj) == np.uint8:
        return format(msj, "08b")

    # Añadimos un raise para controlar que el tipo de datos es correcto
    else:
        raise TypeError("Tipo de datos no soportado.")

# En esta función ocultamos el mensaje en la imagen (ambos parámetros de la función)
def esconder_datos(img, msj_secreto):
    
    n_bytes = img.shape[0] * img.shape[1] * 3 // 8

    # De la misma forma que hicimos antes, usamos de nuevo un raise por si el tamaño de la imagen no es suficiente como
    # para ocultar el mensaje deseado
    if len(msj_secreto) > n_bytes:
        raise ValueError("No hay bytes suficientes. Es necesario una imagen mayor o un mensaje mas corto.")

    msj_secreto += "#####"

    indice = 0
    msj_binario = mensaje_a_binario(msj_secreto)

    data_len = len(msj_binario)
    for valores in img:
        for pixel in valores:
            r, g, b = mensaje_a_binario(pixel)
            if indice < data_len:
                pixel[0] = int(r[:-1] + msj_binario[indice], 2)
                indice += 1
            if indice < data_len:
                pixel[1] = int(g[:-1] + msj_binario[indice], 2)
                indice += 1
            if indice < data_len:
                pixel[2] = int(b[:-1] + msj_binario[indice], 2)
                indice += 1
            if indice >= data_len:
                break

    return img

# Esta función devuelve los decodifica y devuelve el mensaje
def enseñar_datos(img):
    datos_binarios = ""
    for valores in img:
        for pixel in valores:
            r, g, b = mensaje_a_binario(pixel)
            datos_binarios += r[-1]
            datos_binarios += g[-1]
            datos_binarios += b[-1]
    
    datos_en_bytes = [datos_binarios[i: i + 8] for i in range(0, len(datos_binarios), 8)]
    decodificado = ""

    for byte in datos_en_bytes:
        decodificado += chr(int(byte, 2))
        
        if decodificado[-5:] == "#####":
            break

    return decodificado[:-5]

# En esta función insertamos el mensaje que queremos ocultar en la imagen (y mostramos la misma)
def insertar_msj():

    nombre_imagen = "proyimag1T.png"

    imagen = cv2.imread(".\proyimag1T.png")
    tamaño = imagen.shape
    alto = tamaño[0]
    ancho = tamaño[1]

    print(f"{nombre_imagen} tiene de {ancho} de ancho y de {alto} de alto.")

    cv2.imshow('Imagen original', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print()

    msj_a_ocultar = input("Introduzca el mensaje de texto a ocultar: ")

    # De nuevo, usamos raise para notificar que no se ha introducido mensaje alguno
    if (len(msj_a_ocultar) == 0):
        raise ValueError('No ha introducido ningún mensaje.')
    print()

    nombre_archivo = "proyimod1T.png"
    imagen_encodeada = esconder_datos(imagen, msj_a_ocultar)
    cv2.imwrite(nombre_archivo, imagen_encodeada)

    print("Insertando texto en la imagen...\n")
    print(f"El fichero {nombre_imagen} es diferente a {nombre_archivo}\n")

    imagen2 = cv2.imread(".\proyimod1T.png")
    cv2.imshow('Con texto oculto', imagen2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# En esta funcion extraemos el mensaje
def extraer_msj():

    archivo_nombre = "proyimod1T.png"
    datos_imagen = cv2.imread(archivo_nombre, 1)

    print("El fichero de la imagen con texto oculto se llama: " + archivo_nombre + "\n")

    datos_a_mostrar = enseñar_datos(datos_imagen)
    
    return datos_a_mostrar

# Esta es la función que usamos para convertir la imagen a una imagen en escala de grises y la mostramos
def convertir_a_grises():

    archivo_nombre = 'proyimag1T.png'
    print("El fichero de la imagen se llama: " + archivo_nombre)
    print("Convirtiendo la imagen a escala de grises...")

    imagen = cv2.imread(archivo_nombre)
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen_gris = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2RGB)

    cv2.imwrite('proyimgr1T.png',imagen_gris)
    cv2.imshow('Escala de grises', imagen_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Finalmente, la opción de salir simplemente imprime un mensaje de finalización (cuando la llamamos desde el menú se cierra el bucle y por tanto finaliza el programa)
def salir():
    print("Opción de SALIR\n")
    print("FIN DEL PROGRAMA")

menu_ppal()