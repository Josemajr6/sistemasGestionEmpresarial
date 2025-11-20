# 7. Escribir una función que reciba una muestra de números en una lista y devuelva
# otra lista con sus cuadrados.

def cuadradosNumeros (numeros):
    numerosCuadrados = []
    for n in numeros:
        numerosCuadrados.append(n * n)
    return numerosCuadrados

numeros = [ 3, 8, 10 ]
print(cuadradosNumeros(numeros))