# 6. Escribir una función que reciba una muestra de números en una lista y devuelva
# su media. (media = suma de todos los valores / número de valores)

def calcularMedia(numeros):
    total = 0
    for n in numeros:
        total += n
    media = total / len(numeros)
    return media

numeros = [ 3, 8, 10 ]
print(calcularMedia(numeros))
