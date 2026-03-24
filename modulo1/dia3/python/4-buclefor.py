# Bucle For: permite repetir sentencias de codigo una determinada cantidad de veces
#for contador in range(1,11,1):
#    print(contador)
    
# Tabla de multiplicar
# Entrada
tabla = int(input("Ingrese la tabla de multiplicar que desea ver :"))
# Proceso
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f'{tabla} x {contador} = {resultado}')    