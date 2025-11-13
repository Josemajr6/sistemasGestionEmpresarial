# 1. Pedir una palabra por teclado e imprimirla 1000 veces por pantalla con espacios intermedios.

palabra = input("Introduce una palabra: ")
cadena = ""
i=1
while i <= 1000:
    i+=1
    cadena += palabra + " "
    
print(cadena)
