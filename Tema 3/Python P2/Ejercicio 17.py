# 17. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
# de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
# mensaje informando de ello.
# Fruta Precio
# Plátano 1,35
# Manzana 0,80
# Pera 0,85
# Naranja 0,70

precios_frutas = {
    "plátano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}


fruta = input("¿Qué fruta quieres comprar? ").lower()


if fruta in precios_frutas:

    kilos = float(input(f"¿Cuántos kilos de {fruta} quieres? "))
        
    precio_kilo = precios_frutas[fruta]
    precio_total = kilos * precio_kilo
        
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total:.2f} €") # :.2f es que tiene dos decimales

else:
    print(f"La fruta {fruta} no está en la lista.")