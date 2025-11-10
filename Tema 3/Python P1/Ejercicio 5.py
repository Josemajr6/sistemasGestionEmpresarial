# 5. Escriba un programa que calcule el área de un triángulo rectángulo, pidiendo al usuario
# la altura y la base. La salida por pantalla debe ser "Un triángulo rectángulo de altura ____
# y base ____, tiene un área de ____" (sustituyendo los espacios en blanco por los valores).
# NOTA. Área=(base·altura)/2

altura = float(input("Introduce la altura: "))
base = float(input("Introduce la base: "))

print(f"Un triángulo rectángulo de altura {altura} y base {base}, tiene un área de {(base * altura) / 2}")
