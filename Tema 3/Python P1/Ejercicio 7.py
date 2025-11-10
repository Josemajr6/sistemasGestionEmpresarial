# 7. Escriba un programa que pida un tiempo en segundos y lo muestre convertido a minutos y segundos.

tiempoSegundos = int(input("Introduce un tiempo en segundos: "))
print(f"{tiempoSegundos} segundos en minutos y segundos es: {round(tiempoSegundos/60)} minutos y {tiempoSegundos%60} segundos")
