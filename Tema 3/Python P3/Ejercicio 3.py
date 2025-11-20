# 3. Escribir una función que reciba un número entero positivo y devuelva su factorial

def factorial(num):
    if num == 0: return 1
    return num * factorial(num - 1)

print(factorial(5))