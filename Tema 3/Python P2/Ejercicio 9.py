# 9. Crea una aplicación que pida un número y calcule su factorial. El factorial de un número
# es el producto de todos los números enteros entre 1 y el ese número y se representa por
# el número seguido de un signo de exclamación. P. ej. 6! = 1x2x3x4x5x6=720. Realiza una
# propuesta con while y otra con for.

numero = int(input("Introduce un número para calcular su factorial: "))

factorial = 1

# Usando While
# i = 1
# while i <= numero:
#     factorial = factorial * i  
#     i += 1                    

# Usando For
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")