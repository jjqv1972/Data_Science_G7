# RETO 1 : CREAR UN PROGRAMA USANDO COMO EJEMPLO EL CODIGO DE LA CALCULADORA 
# QUE PERMITA CONVERTIR EL VALOR DE UNA MONEDA DE SOLES A DOLARES Y VICEVERSA,
# POR EJEMPLO SI INGRESO CONVERTIR SOLES A DOLARES E INGRESO 3000 SOLES 
# DEBERIA MOSTRARME SU VALOR EN DOLARES QUE SERIA 1000 DOLARES CONSIDERANDO 
# QUE EL TIPO DE CAMBIO ES 3
# =============================================
#                        CONVERTIDOR DE MONEDAS
#            =============================================
#                    [1] CONVERTIR SOLES A DOLARES
#                    [2] CONVERTIR DOLARES A SOLES
#                    [3] SALIR
#            =============================================

itcambio=3

salir = "no"

while(salir=="no"):
    # Entrada
    print("===CONVERSION DE MONEDAS===")

    print("======= OPCIONES ==========")
    print("1. Soles a Dolares")
    print("2. Dolares a Soles")
    opcion = int(input("Ingrese la opcion que desea: "))

    # Proceso
    if opcion==1:
        # Soles a Dolares
        print(" Se procederá a cambiar Soles a Dolares")
        nummon = float(input(" Ingresar valor en soles: "))
        resul = nummon / itcambio
        print(f" El cambio de {nummon} soles es de :{resul:.2f} dolares")

    elif opcion==2:
        # Dolares a Soles
        print(" Se procederá a cambiar Dolares a Soles")
        nummon = float(input(" Ingresar valor en dolares: "))
        resul = nummon * itcambio
        print(f" El cambio de {nummon} dolares es de : {resul:.2f} soles")
    else:
        print("Opción no valida...")


    # Salida

    salir = input("Desea salir del programa? (si,no) : ")
    if salir == "si":
        break
