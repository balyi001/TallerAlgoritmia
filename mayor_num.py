print("Digite el Primer numero")
num1 = float(input())
print("Digite el Segundo numero")
num2 = float(input())
print("Digite el Tercer numero")
num3 = float(input())

if num1 > num2:
    if num1 > num3:
        mayor = num1
        mayor_nombre = "Primer numero"
    else:
        mayor = num3
        mayor_nombre = "Tercer numero"
else:
    if num2 > num3:
        mayor = num2
        mayor_nombre = "Segundo numero"
    else:
        mayor = num3
        mayor_nombre = "Tercer numero"

print("El numero mayor es:", mayor, "El cual es el", mayor_nombre)