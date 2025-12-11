print("Digite el valor de la compra")
valorCompra = float(input())

if valorCompra > 100000:
    descuento = valorCompra * 0.1
else:
    descuento = 0

valorFinal = valorCompra - descuento
print("Valor total a pagar: $", valorFinal)