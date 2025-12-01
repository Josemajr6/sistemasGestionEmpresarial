# 14. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre
# por pantalla en orden inverso separados por comas.

numeros = []
for i in range(1, 11):
    numeros.append(i)

numeros.reverse()

textoAMostrar = ""

for i in range(len(numeros)):
    if i != len(numeros)-1:
        textoAMostrar += str(numeros[i]) + ", "
    else:
        textoAMostrar += str(numeros[i]) + "."

print(textoAMostrar)