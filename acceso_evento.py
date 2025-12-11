contador_mayores = 0
contador_menores = 0

mas_usuarios = True

print("--- Sistema de Control de Acceso al Evento ---")

while mas_usuarios:
    print("--------------------------------------------")
    print("Ingrese la edad del siguiente usuario (o -1 para terminar la fila):")
    edad = int(input())
    
    if edad == -1:
        mas_usuarios = False
    else:
        if edad > 0:
            if edad >= 18:
                print("El usuario con", edad, "años es **MAYOR DE EDAD**.")
                print("**¡Puede ingresar al evento!**")
                contador_mayores = contador_mayores + 1
            else:
                print("El usuario con", edad, "años es **MENOR DE EDAD**.")
                print("**NO puede ingresar al evento.**")
                contador_menores = contador_menores + 1
        else:
            print("Error: La edad ingresada no es válida. Por favor, intente de nuevo.")

print("--------------------------------------------")
print("--- **RESUMEN DEL EVENTO** ---")
print("Total de personas mayores de edad que intentaron ingresar:", contador_mayores)
print("Total de personas menores de edad que intentaron ingresar:", contador_menores)
print("Total de personas procesadas:", contador_mayores + contador_menores)
print("--------------------------------------------")