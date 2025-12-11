dias_semana = 6

print("Ingrese el gasto diario en pasajes:")
pasaje_diario = float(input())

print("Ingrese el gasto diario en refrigerio:")
refrigerio_diario = float(input())

gasto_diario_total = pasaje_diario + refrigerio_diario

gasto_semanal = gasto_diario_total * dias_semana

print("--- Resultado ---")
print("El gasto diario total es de: $", gasto_diario_total)
print("El total semanal gastado (de lunes a sábado) es de: $", gasto_semanal)