import cv2
from random import randint
from PIL import Image

# FUNCIÓN PARA INSERTAR MENSAJE OCULTO EN IMAGEN
def op1():
    print(" OPCIÓN: Insertar mensaje oculto en una imagen")
    #Introducimos el alfabeto adaptado al teclado en español
    alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789~`!@#$%^&*()_+-=.,'*/ "
    #Empezamos leyendo el archivo original
    img_data = cv2.imread('original.png')

    def encrypt(mes, img):
        num = []
        locs = []

        for i in mes:
            num.append(alpha.index(i))
        for i in range(len(num)):
            locs.append((randint(0, len(img_data) - 1), randint(0, len(img_data[0]) - 1), randint(0, 2)))
        for i, j in zip(locs, num):
            img_data[i[0]][i[1]][i[2]] = j

        return cv2.imwrite('new.png', img_data), locs
    print("proyimag1T.png tiene de", img_data.shape[0], " de ancho y de", img_data.shape[1], "de alto")
    print("Para salir de la ventana pulse una tecla o cierre manualmente")
    cv2.imshow('helloworld', img_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Introduzca el mensaje de texto a ocultar: ")
    img_new, locs = encrypt(input(), 'original.png')
    img_data2 = cv2.imread('new.png')
    img1 = Image.open(r"original.png")
    img2 = Image.open(r"new.png")
    # using tobytes
    img1.tobytes("hex", "rgb")
    img2.tobytes("hex", "rgb")
    if img1 == img2:
        print("El fichero proyimag1T.png no es diferente a proyimod1T.png")
    else:
        print("El fichero proyimag1T.png es diferente a proyimod1T.png")

    print("Para salir de la ventana pulse una tecla o cierre manualmente")
    cv2.imshow('helloworld', img_data2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# FUNCIÓN PARA EXTRAER MENSAJE OCULTO DE UNA IMAGEN
#def op2(img, locs):
#    img_data = cv2.imread(img, 1)
#    str_ = ""
#    for i in locs:
#        str_ += alpha[img_data[i[0]][i[1]][i[2]]]
#
#   return str_
#
#
#print(op2('new.png', locs))

# FUNCIÓN PARA PASAR LA IMAGEN A ESCALA DE GRISES
def op3():
    imagen = cv2.imread('proyimag1T.png')
    print("Convirtiendo la imagen a escala de grises...")
    img_engris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    img_engris = cv2.cvtColor(img_engris, cv2.COLOR_GRAY2RGB)
    cv2.imwrite('proyimag1T_gris.png',img_engris)
    cv2.imshow('Escala de grises', img_engris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# AQUI EMPIEZA EL MENU
def menu():
    print("Selecciona una opción")
    print("\t1 - [1] Insertar mensaje oculto en una imagen")
    print("\t2 - [2] Extraer mensaje oculto de una imagen")
    print("\t3 - [3] Convertir la imagen a escala de grises")
    print("\t4 - [4] Salir")

menu()
opcion = int(input("Introduce la opción deseada: "))

while opcion != 4:
    if opcion == 1:
        print("Ha elegido: Insertar mensaje oculto en una imagen")
        op1()
    elif opcion == 2:
        print("Ha elegido: Extraer mensaje oculto de una imagen")
        op2()
    elif opcion == 3:
        print("Ha elegido: Convertir la imagen a escala de grises")
        op3()
# SI EL USUARIO ELIGE (4) SE CIERRA EL BUCLE Y APARECE UN MENSAJE DE ERROR, VUELVE A APARECER EL MENU
    else:
        print("Opción no valida.")
    print()
    menu()
    opcion = int(input("Introduce la opción deseada: "))
print("Gracias por usar nuestro programa. Adios.")