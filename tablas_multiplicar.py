print("Ingrese el número del cual desea ver la tabla de multiplicar:")
num = int(input())

print("-------------------")
print("Tabla de Multiplicar del", num, ":")
print("-------------------")

for i in range(1, 11):
    resultado = num * i
    print(num, "x", i, "=", resultado)

print("-----------------")
print("Fin de la tabla.")