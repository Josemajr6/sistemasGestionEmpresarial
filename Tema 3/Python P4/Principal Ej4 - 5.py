from Empresa import Empresa
from Empleado import Empleado

listaEmpresas = []

while True:
    print("¿Que quieres hacer? ")
    print("1. Crear empresa")
    print("2. Listar empresas")
    print("3. Eliminar empresa")
    print("4. Listar empresas con menos de 10 empleados")
    print("5. Listar empresas con 10 o más empleados")
    print("6. Procesar empleados de una empresa")
    print("7. Salir")
    
    opcion = int(input("Selecciona una opcion: "))
    
    match opcion:
        case 1:
            nombre = input("Introduce el nombre de la empresa: ")
            direc = input("Introduce la dirección de la empresa: ")
            industria = input("Introduce la industria de la empresa: ")
            telefono = input("Introduce el teléfono de la empresa: ")
            correo = input("Introduce el correo de la empresa: ")
            listaEmpresas.append(Empresa(nombre, direc, industria, telefono, correo))
            print(f"Se ha creado la empresa {nombre}")
        
        case 2:
            print("Lista de empresas")
            cont = 0
            for e in listaEmpresas:
                cont = cont + 1 
                print(f"{cont}. {e}")
        
        case 3:
            print("Lista de empresas")
            cont = 0
            for e in listaEmpresas:
                cont = cont + 1 
                print(f"{cont}. {e}")
            
            num_borrar = int(input("Selecciona el número de la empresa que desea borrar: "))
            if num_borrar > 0 and num_borrar <= len(listaEmpresas):
                listaEmpresas.pop(num_borrar - 1)
                print("Se ha borrado la empresa")
            else:
                print("No existe la empresa que has introducido")
                
        case 4:
            print("Lista de empresas con menos de 10 empleados")
            cont = 0
            for e in listaEmpresas:
                cont = cont + 1
                if len(e.empleado) < 10:
                    print(f"{cont}. {e}")
        
        case 5:
            print("Lista de empresas con 10 o más empleados")
            cont = 0
            for e in listaEmpresas:
                cont = cont + 1
                if len(e.empleado) >= 10:
                    print(f"{cont}. {e}")
        
        case 6:
            print("Lista de empresas")
            cont = 0
            for e in listaEmpresas:
                cont = cont + 1 
                print(f"{cont}. {e}")
            
            num_empresa = int(input("Selecciona el número de la empresa: "))
            
            if num_empresa > 0 and num_empresa <= len(listaEmpresas):
                empresa_seleccionada = listaEmpresas[num_empresa - 1]
                
                while True:
                    print(f"Gestionando empresa: {empresa_seleccionada.nombre}")
                    print("¿Que quieres hacer? ")
                    print("1. Agregar empleado")
                    print("2. Eliminar empleado")
                    print("3. Despedir empleado")
                    print("4. Calcular costo salarial")
                    print("5. Listar empleados")
                    print("6. Filtrar empleados por edad")
                    print("7. Filtrar empleados por cargo")
                    print("8. Filtrar empleados por salario")
                    print("9. Volver atrás")
                    
                    opcionE = int(input("Selecciona una opcion: "))
                    
                    match opcionE:
                        case 1:
                            idEmp = input("Introduce ID Empleado: ")
                            nom = input("Introduce Nombre: ")
                            ed = int(input("Introduce Edad: "))
                            car = input("Introduce Cargo: ")
                            sal = float(input("Introduce Salario: "))
                            fech = input("Introduce Fecha Contratación: ")
                            corr = input("Introduce Correo: ")
                            tel = input("Introduce Teléfono: ")
                            dir = input("Introduce Dirección: ")
                            hor = input("Introduce Horario: ")
                            empresa_seleccionada.agregar_empleado(Empleado(idEmp, nom, ed, car, sal, fech, corr, tel, dir, hor))
                        
                        case 2:
                            id_borrar = input("Introduce el ID del empleado a eliminar: ")
                            empresa_seleccionada.eliminar_empleado(id_borrar)
                            
                        case 3:
                            id_despedir = input("Introduce el ID del empleado a despedir: ")
                            encontrado = False
                            for emp in empresa_seleccionada.empleado:
                                if emp.id_empleado == id_despedir:
                                    emp.Despedir()
                                    encontrado = True
                            if encontrado == False:
                                print("No se ha encontrado el empleado")

                        case 4:
                            total = empresa_seleccionada.calcular_costo_salarial()
                            print(f"El costo salarial total es: {total}")
                            
                        case 5:
                            empresa_seleccionada.listar_empleados()
                            
                        case 6:
                            min_edad = int(input("Introduce edad mínima: "))
                            max_edad = int(input("Introduce edad máxima: "))
                            for emp in empresa_seleccionada.empleado:
                                if emp.contrato == True and emp.edad >= min_edad and emp.edad <= max_edad:
                                    print(emp)
                                    
                        case 7:
                            cargo_buscar = input("Introduce el cargo: ")
                            for emp in empresa_seleccionada.empleado:
                                if emp.contrato == True and emp.cargo == cargo_buscar:
                                    print(emp)
                                    
                        case 8:
                            salario_min = float(input("Introduce salario mínimo: "))
                            for emp in empresa_seleccionada.empleado:
                                if emp.contrato == True and emp.salario > salario_min:
                                    print(emp)
                                    
                        case 9:
                            break
            else:
                print("Número de empresa incorrecto")

        case 7:
            break