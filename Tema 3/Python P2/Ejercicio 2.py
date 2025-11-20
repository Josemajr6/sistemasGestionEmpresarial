# 2. Pedir un número por teclado, e indicar por pantalla, si es positivo, negativo o cero.

num = float(input("Introduce un número: "))

if num > 0:
    print("Es positivo")
elif num == 0:
    print("Es cero")
else:
    print("Es negativo")