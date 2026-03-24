# Calculadora
# Crear un programa que permita sumar, restar, multiplicar o dividir dos numeros
# dependiendo del tipo de operación que se indique
# Entrada
numero1 = int(input("Número1:"))
numero2 = int(input("Número2:"))
operacion = input("Ingrese operación (+ - x /):")

# Proceso
if operacion=="+":
    # Suma
    resultado = numero1 + numero2
elif operacion=="-":
    # Resta
    resultado = numero1 - numero2
elif operacion=="x":
    # Resta
    resultado = numero1 * numero2
elif operacion=="/":
    # Resta
    resultado = numero1 / numero2
else:
    print("Operación no valida...")
    exit()
    
# Salida
print(f"{numero1} {operacion} {numero2} = {resultado}")
    

