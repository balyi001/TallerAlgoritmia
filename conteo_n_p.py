positivos = 0
negativos = 0

for i in range(1, 6):
    print("Digite un numero")
    num = int(input())
    if num >= 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1

print("Positivos:", positivos, "Negativos:", negativos)