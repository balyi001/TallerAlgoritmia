print("Ingrese un número entero positivo:")
num = int(input())

if num < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    
    print("El factorial de", num, "es:", factorial)