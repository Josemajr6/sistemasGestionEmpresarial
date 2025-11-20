# 10. Crea una aplicación que permita adivinar un número. En primer lugar, la aplicación
# solicita un número entero por teclado, que será el número que debe adivinarse. A
# continuación, va pidiendo números y va indicando por pantalla, si el número a adivinar
# es mayor o menor que el introducido. El programa termina cuando se acierta el número.

num = int(input("Introduce un número (para que lo adivinen): "))


intento = 0
if (num == 0): intento - 1

while (intento != num):
    intento = int(input("Introduce un número a ver si adivinas: "))
    if intento == num:
        print("Has acertado")
    elif intento < num:
        print("Es número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")


