# 4. Escriba un programa que calcule el interés que se obtiene por un determinado dinero
# depositado en un banco. Para ello el programa preguntará por el capital inicial y por el
# tipo de interés.

capital = float(input("Introduce el capital inicial: "))
interes = float(input("Introduce el interés: "))

print(f"El banco se quedará con un interés de: {capital * (interes / 100)}")

