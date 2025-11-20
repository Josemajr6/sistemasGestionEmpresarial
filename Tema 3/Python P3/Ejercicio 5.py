# 5. Escribir una función que calcule el área de un círculo y otra que calcule el
# volumen de un cilindro usando la primera función. (área_círculo = pi·r2; volumen_cilindro = pi·r2·h)

import math

def areaCirculo(radio):
    return math.pi * (radio * radio)

def volumenCilindro(radio, altura):
    return areaCirculo(radio * altura)

print(volumenCilindro(50, 100))