# 8. Pedir un número por teclado y mostrar la tabla de multiplicar. 
# Realiza una solución con while y otra con for.

num = int(input("Introduce un número: "))

# Usando While
# i = 0
# while i <= 10:
#     print(num, "*", i, " = ", (num * i))
#     i+=1

# Usando For
for i in range(11):
    print(num, "*", i, " = ", (num * i))