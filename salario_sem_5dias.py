totalHorasSemana = 0

print("Ingrese el valor por hora:")
valorHora = float(input())

for i in range(1, 6):
    print("Ingrese las horas trabajadas del día", i, ":")
    horasTrabajadasDia = float(input())
    totalHorasSemana = totalHorasSemana + horasTrabajadasDia

print("Total de horas trabajadas en la semana:", totalHorasSemana)

salarioBase = totalHorasSemana * valorHora
salarioTotal = salarioBase

if totalHorasSemana > 40:
    extra = (totalHorasSemana - 40) * valorHora * 0.5
    salarioTotal = salarioTotal + extra
    
    print("Se trabajaron", (totalHorasSemana - 40), "horas extras.")
    print("Monto por horas extras (recargo):", extra)

print("--- Resultado ---")
print("Salario Base (por todas las horas a tarifa normal):", salarioBase)
print("Salario total (con recargo de extras si aplica):", salarioTotal)