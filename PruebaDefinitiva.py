import cv2
from random import randint
from PIL import Image

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
    print("instroduzca el mensaje de texto a ocultar: ")
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

op1()
#esta es la funcion para descryptear
'''
def decrypt(img, locs):
    img_data = cv2.imread(img, 1)
    str_ = ""
    for i in locs:
        str_ += alpha[img_data[i[0]][i[1]][i[2]]]

    return str_


print(decrypt('new.png', locs))
'''