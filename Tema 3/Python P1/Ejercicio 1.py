# 1. Escriba un programa que muestre en la pantalla un mensaje de saludo, por ejemplo
# "Hola, y luego muestre el mensaje "Por favor introduzca el año en que nació". El
# programa debe leer ese valor y almacenarlo en una variable llamada fecha. Por último,
# haga que el programa escriba la frase " Si usted nació en este año cumple ___ años”.  

anioActual = 2025
print('Hola')
fecha = input('Por favor introduzca el año en que nació: ')
print(f'Si usted nació en {fecha} este año cumple {anioActual - int(fecha)} años')