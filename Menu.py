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
        extraerMensaje()
    elif opcion == 3:
        print("Ha elegido: Convertir la imagen a escala de grises")
        pasarAgris()

        '''SI EL USUARIO ELIGE (4) SE CIERRA EL BUCLE Y APARECE UN MENSAJE DE ERROR, VUELVE A APARECER EL MENU'''
    else:
        print("Opción no valida")
    print()
    menu()
    opcion = int(input("Introduce la opción deseada: "))

print("Gracias por usar el programa. Adios.")

