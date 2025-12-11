for i in range(1, 6):
    print("--- Estudiante", i, "---")
    
    print("Ingrese la Nota 1:")
    nota1 = float(input())
    print("Ingrese la Nota 2:")
    nota2 = float(input())
    print("Ingrese la Nota 3:")
    nota3 = float(input())
    
    prom = (nota1 + nota2 + nota3) / 3
    
    if prom >= 3.0:
        print("#### Aprobó con:", prom)
    else:
        print("#### Reprobó con:", prom)