# 4. Escribir una función que calcule el total de una factura tras aplicarle el IVA. La
# función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver
# el total de la factura. Si se invoca la función sin pasarle el porcentaje sin IVA,
# deberá aplicar un 21%

def calcularIVA(cantidad, porcentaje = 21):
    total = cantidad + (cantidad * (porcentaje / 100))
    return total

cantidad = 1000
print(f"Factura 1: {cantidad}\nIncluyendo IVA: {calcularIVA(cantidad, 30)}")