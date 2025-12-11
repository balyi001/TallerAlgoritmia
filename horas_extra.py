print("Horas trabajadas")
horasTrabajadas = float(input())
print("Valor de la hora trabajada")
valorHora = float(input())

salario = horasTrabajadas * valorHora

if horasTrabajadas > 40:
    extra = (horasTrabajadas - 40) * valorHora * 0.5
    salario = salario + extra

print("Salario total: $", salario)