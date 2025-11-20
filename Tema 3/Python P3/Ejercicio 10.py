# 10. Escribir una función que convierta un número decimal en binario y otra que
# convierta un número binario en decimal.

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

def binario_a_decimal(binario):
    binario = str(binario)
    decimal = 0
    
    longitud = len(binario)
    
    for i in range(longitud):
        digito = binario[i]
        
        if digito == '1':
            exponente = longitud - 1 - i
            decimal = decimal + (2 ** exponente)
            
    return decimal

print(decimal_a_binario(25))
print(binario_a_decimal("11001"))