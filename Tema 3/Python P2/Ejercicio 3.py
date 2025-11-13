# 3. Amplia el ejercicio anterior, y pide por pantalla 2 números. Comprueba si la suma de los
# dos números es positiva, negativa o cero.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if (num1+num2) > 0:
    print("La suma es positiva")
elif (num1+num2) == 0:
    print("La suma da 0 como resultado")
else:
    print("La suma es negativa")