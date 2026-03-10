import os
from time import sleep

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""
ANCHO = 50

dic_alumnos = {
    '12345678':{
        'nombre':'Juan Perez',
        'email':'juanperez@gmail.com'
    },
    '10010010':{
        'nombre':'Ana Lopez',
        'email':'analopez@gmail.com'
    }
}

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR ALUMNO")
        print("=" * ANCHO)
        
        codigo = input("INGRESE DNI : ")
        nombre = input("INGRESE NOMBRE : ")
        email = input("INGRESE EMAIL : ")
        dic_nuevo_alumno = {
            'nombre':nombre,
            'email':email
        }
        dic_alumnos[codigo] = dic_nuevo_alumno
        print("Alumno registrado exitosamente.")
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR ALUMNOS")
        print("=" * ANCHO)
        
        for codigo,info in dic_alumnos.items():
            print(f"DNI : {codigo}")
            print(f"NOMBRE : {info['nombre']}")
            print(f"EMAIL : {info['email']}")
            print("*"*ANCHO)
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR ALUMNO")
        print("=" * ANCHO)
        codigo = input("INGRESE DNI DEL ALUMNO: ")
      
        if codigo in dic_alumnos:
            print(f"Alumno encontrado : {dic_alumnos[codigo]['nombre']}")
            print("Ingrese nuevos datos para el alumno o presionar enter para conservar datos anteriores ...")
            nuevo_nombre = input("INGRESE NUEVO NOMBRE ({dic_alumnos[codigo]['nombre']}): ")
            nuevo_email = input("INGRESE NUEVO EMAIL ({dic_alumnos[codigo]['email']}): ")
            if nuevo_nombre:
                dic_alumnos[codigo]['nombre']=nuevo_nombre
            if nuevo_email:
                dic_alumnos[codigo]['email']=email
            print("Alumno actualizado exitosamente.")
        else:
            print(" " * 10 + "NO SE TIENE DNI INGRESADO EN LOS REGISTROS")
        print("=" * ANCHO)                                
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR ALUMNO")
        print("=" * ANCHO)
        
        codigo = input("INGRESE DNI : ")
        if codigo in dic_alumnos:
            del dic_alumnos[codigo]     #         dic_alumnos.pop(codigo)
            print("Alumno eliminado exitosamente.")
        else:
            print(" " * 10 + "NO SE TIENE DNI INGRESADO EN LOS REGISTROS")
        print("=" * ANCHO)                                    
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")