contador_positivos = 0
numero_ingresado = 1

while numero_ingresado != 0:
    print("Ingrese un número (ingrese 0 para finalizar):")
    numero_ingresado = int(input())
    
    if numero_ingresado > 0:
        contador_positivos = contador_positivos + 1

print("----------------------")
print("Se ingresaron", contador_positivos, "números positivos.")
print("Algoritmo finalizado.")