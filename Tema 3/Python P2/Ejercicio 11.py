# 11. Programa que muestre la tabla de multiplicar del número que introduzcas por teclado.

num = int(input("Introduce un número: "))

# Usando While
# i = 0
# while i <= 10:
#     print(num, "*", i, " = ", (num * i))
#     i+=1

# Usando For
for i in range(11):
    print(num, "*", i, " = ", (num * i))