# 9. Escriba un programa que convierta euros a dólares (1 euro = 1.16 dólares) y a libras
# esterlinas (1 euro = 0,88 libras). Imprima los resultados por pantalla.

euros = float(input("Introduce una cantidad de euros: "))
dolares = euros * 1.16;
libras = euros * 0.88;
print(f"{euros} euros serían {dolares} dólares y {libras} libras esterlinas.")


