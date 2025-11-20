# 18. Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las
# facturas se almacenarán en un diccionario donde la clave de cada factura será el número
# de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere
# añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva
# factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si
# se desea pagar una factura se preguntará por el número de factura y se eliminará del
# diccionario. Después de cada operación el programa debe mostrar por pantalla la
# cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

facturas_pendientes = {}
total_cobrado = 0.0

while True:
    print("\n--- GESTIÓN DE FACTURAS ---")
    print("1. Añadir una nueva factura")
    print("2. Pagar una factura existente")
    print("3. Terminar")
    
    opcion = input("Elige una opción (1, 2, 3): ")

    if opcion == '1':
        num_factura = input("Introduce el número de factura: ")
        if num_factura in facturas_pendientes:
            print(f"Error: La factura {num_factura} ya existe.")
        else:
            coste = float(input("Introduce el coste de la factura: "))
            if coste < 0:
                print("Error: El coste no puede ser negativo.")
            else:
                facturas_pendientes[num_factura] = coste
                print(f"Factura {num_factura} añadida correctamente.")
    
    elif opcion == '2':
        num_factura = input("Introduce el número de factura a pagar: ")
        
        if num_factura in facturas_pendientes:
            coste_pagado = facturas_pendientes.pop(num_factura)
            total_cobrado += coste_pagado
            print(f"Factura {num_factura} pagada (Coste: {coste_pagado:.2f} €).")
        else:
            print(f"Error: La factura {num_factura} no existe.")
            
    elif opcion == '3':
        print("Cerrando el programa...")
        break 
        
    else:
        print("Opción no válida. Por favor, introduce 1, 2 o 3.")

    
    total_pendiente = sum(facturas_pendientes.values())
    
    print("\n--- RESUMEN ACTUAL ---")
    print(f"Cantidad cobrada hasta el momento: {total_cobrado:.2f} €")
    print(f"Cantidad pendiente de cobro: {total_pendiente:.2f} €")
    print(f"Facturas pendientes: {facturas_pendientes}")
    print("-------------------------")

print(f"\nResumen final: Total cobrado = {total_cobrado:.2f} €")