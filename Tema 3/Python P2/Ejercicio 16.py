# 16. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
# guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
# tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu teléfono: ")

datos = dict(nombre = nombre, edad = edad, direccion = direccion, telefono = telefono)

print(f"{datos.get('nombre')} tiene {datos.get('edad')} años, vive en {datos.get('direccion')} y su número de teléfono es {datos.get('telefono')}")