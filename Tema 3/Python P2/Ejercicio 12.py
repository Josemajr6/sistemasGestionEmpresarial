# 12. Escribe un programa que diga si un número introducido por teclado es o no primo. Un
# número primo es aquel que sólo es divisible entre él mismo y la unidad.

num = int(input("Introduce un número y te diré si es o no es primo: "))

esPrimo = True

if num == 1 | num == 2:
    esPrimo = True
elif num < 1:
    esPrimo = False
else:
    for i in range(2, num):
        if num % i == 0:
            esPrimo = False
            break

print(f"Es primo" if esPrimo else "No es primo")