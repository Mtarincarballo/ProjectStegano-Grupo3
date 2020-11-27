import cv2

## Pasar imagen a gris
def pasarAgris():
    imagen = cv2.imread('proyimag1T.png')
    print("Convirtiendo la imagen a escala de grises...")
    img_engris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    img_engris = cv2.cvtColor(img_engris, cv2.COLOR_GRAY2RGB)
    cv2.imwrite('proyimag1T_gris.png',img_engris)
    cv2.imshow('Escala de grises', img_engris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()