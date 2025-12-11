print("Digite las notas del estudiante")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

prom = (nota1 + nota2 + nota3) / 3

if prom >= 3.0:
    print('Aprobó con:', prom)
else:
    print('Reprobó con:', prom)