# 9. Escribir una función que reciba una muestra de una lista y devuelva un
# diccionario con su media, su varianza y su desviación típica. 

def calcular_estadisticas(lista):
    # Guardamos la cantidad de datos (n)
    n = len(lista)
    

    if n < 2:
        return None


    media = sum(lista) / n
    suma_diferencias = 0
    for x in lista:
        suma_diferencias += (x - media) ** 2
        
    varianza = suma_diferencias / (n - 1)

    desviacion = varianza ** 0.5

    return {
        "media": round(media, 2),
        "varianza": round(varianza, 2),
        "desviacion_tipica": round(desviacion, 2)
    }

mis_datos = [10, 12, 23, 23, 16, 23, 21, 16]
resultado = calcular_estadisticas(mis_datos)

print(f"Lista de números: {mis_datos}")
print(resultado)