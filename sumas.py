suma = 0

print("=== Suma de números (ingrese 0 para terminar) ===")
print("Ingrese un número:")
num = float(input())

while num != 0:
    suma = suma + num
    print("Ingrese otro número (0 para finalizar):")
    num = float(input())

print("La suma total de los números ingresados es:", suma)