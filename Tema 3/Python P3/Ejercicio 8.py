# 8. Escribir una función que calcule el máximo común divisor de dos números y otra
# que calcule el mínimo común múltiplo. (MCD = factores comunes elevado al
# exponente más pequeño; mcm = factores comunes y no comunes elevado al máximo exponente).


def calcular_mcd(a, b):
    while b > 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def calcular_mcm(a, b):
    if a == 0 or b == 0:
        return 0
    
    producto = a * b
    mcd = calcular_mcd(a, b)
    return producto / mcd


print(calcular_mcd(24, 36))
print(calcular_mcm(24, 36))