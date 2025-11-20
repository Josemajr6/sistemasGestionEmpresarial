# 15. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.


abecedario = list("abcdefghijklmnñopqrstuvwxyz")

for i in range(len(abecedario) -2 ,-0, -3):
    abecedario.pop(i)

print(abecedario)