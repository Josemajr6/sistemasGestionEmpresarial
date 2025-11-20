# 4. Recoge por teclado un número que represente un número del mes del año, y que indique
# por pantalla el número de días que tiene dicho mes. Incluye la validación necesaria para
# que el usuario introduzca un mes válido y en caso contrario, deberás avisar por pantalla.

mes = int(input("Introduce el mes del año como número: "))


match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12: 
        print("El mes tiene 31 días")
    case 4 | 6 | 9 | 11:
        print("El mes tiene 30 días")
    case 2:
        print("El mes tiene 28 días")
    case _:
        print("Introduce un número entre 1 y 12")


    