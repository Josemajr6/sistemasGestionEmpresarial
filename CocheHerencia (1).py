#Esta clase define el estado y comportamiento de un coche
class Coche:

    #Atributo de clase. Atributo estático
    contadorcoches = 0


    def __init__(self, color, marca, modelo):

        self.color = color
        self.aceleracion = 0
        self.velocidad = 0

        self.marca = marca
        self.modelo = modelo
        self.matricula = ""

        Coche.contadorcoches += 1

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

#Método para acelerar
    def acelerar (self,aceleracion):
        self.rugir()
        self.aceleracion=aceleracion
        self.velocidad = self.velocidad + aceleracion

#Método para frenar
    def frenar (self,aceleracion):
        v = self.velocidad - aceleracion
        self.aceleracion=aceleracion

        if v < 0:
            v=0

        self.velocidad=v

#Método para rugir
    def rugir(self):
        print ("Brrrrrrr")
        
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h"



# Puede haber otra clase en el mismo fichero

#La clase hoja, lleva entre paréntesis el nombre de la clase padre.
#cochemarchas lleva el nombre de la clase coche en su declaración
class Cochemarchas(Coche):

    def __init__(self,marchas,color, marca, modelo):
        super().__init__(color, marca, modelo)
        #marchas indica el número de marchas hacia delante
        self.marchas=marchas

        # 0 significa que está en punto muerto
        # -1 significa que está en marcha atrás
        self.marchaactual=0

        self.frenomano=True
        
    def get_marchas_totales(self):
        return self.marchas

    def get_marcha_actual(self):
        return self.marchaactual


    def cambiomarcha(self, nuevamarcha):
        if nuevamarcha == -1 and (self.velocidad > 0 or self.marchaactual != 0):
            print ("Error: Para marcha atrás el coche debe estar parado y en punto muerto")
            return
        
        if nuevamarcha >= 4 and self.velocidad < 20:
            print("El coche se ha callado")
            self.velocidad = 0
            self.marchaactual = 0
            return
        
        if nuevamarcha <= 2 and self.velocidad > 80:
            print("Aviso: El coche está muy revolucionado")
            
        self.marchaactual = nuevamarcha
        print(f"Has cambiado a la marcha {self.marchaactual}")

    def ponerpuntomuerto(self):
        self.marchaactual = 0
        print("El coche está en punto muerto")

    def ponerfrenomano(self):
        if self.velocidad > 0:
            print("No se puede poner el freno de mano en movimiento")
        else:
            self.frenomano = True
            print("Freno de mano activado")    
        

    def quitarfrenomano(self):
        self.frenomano = False
        print("Freno de mando quitado")
    
    def rugir(self):
        if self.marchaactual == 0:
            print("shhh")
        else:
            print("¡¡POOOMM!!")
            
            
    def __str__(self):
        return super().__str__() + f", Marcha: {self.marchaactual}/{self.marchas}, Freno Mano: {self.frenomano}"

class Cocheautomatico(Coche):
    def __init__(self, color, marca, modelo):
        super().__init__(color, marca, modelo)
        self.modo = 'P'

    def get_modo(self):
        return self.modo

    def cambiarmodo(self, nuevo_modo):
        nuevo_modo = nuevo_modo.upper() 
        valoresmodos = ['P', 'R', 'N', 'D']
        
        if nuevo_modo in valoresmodos:
            self.modo = nuevo_modo
            print(f"Modo automático cambiado a: {self.modo}")
        else:
            print("Modo inválido. Usa P, R, N o D")
            
    def rugir(self):
        if self.modo == 'P' or self.modo == 'N':
            print("...")
        elif self.modo == 'R':
            print("Piiii... Pii... Pi.....")
        elif self.modo == 'D':
            print("Sshhhhhhh tssss")
    
    def __str__(self):
        return super().__str__() + f", Modo: {self.modo}"
            

class Tecnico():
    def __init__(self, nombre, cargo, especialidad):
        self.nombre = nombre
        self.cargo = cargo
        self.especialidad = especialidad
        self.vacaciones = False
        self.baja = False
        self.tipos_reparaciones = []
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
        
    def get_especialidad(self):
        return self.especialidad
    
    def set_especialidad(self, especialidad):
        self.especialidad = especialidad
    
    def get_vacaciones(self):
        return self.vacaciones

    def set_vacaciones(self, vacaciones):
        self.vacaciones = vacaciones

    def get_baja(self):
        return self.baja

    def set_baja(self, baja):
        self.baja = baja

    def get_tipos_reparaciones(self):
        return self.tipos_reparaciones

    def set_tipos_reparaciones(self, tipos_reparaciones):
        self.tipos_reparaciones = tipos_reparaciones
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Especialidad: {self.especialidad}, Vacaciones: {self.vacaciones}, Tipos reparaciones: {self.tipos_reparaciones}"

    def cogervacaciones(self):
        if self.vacaciones:
            print("El técnico ya está de vacaciones")
        else:
            self.vacaciones = True
            print(f"El técnico {self.nombre} ha cogido vacaciones")

    def volvervacaciones(self):
        if not self.vacaciones:
            print("El técnico no está de vacaciones")
        else:
            self.vacaciones = False
            print(f"El técnico {self.nombre} ha vuelto de vacaciones")
            
    def dardebaja(self):
        if self.baja:
            print("El técnico ya está de baja.")
        else:
            self.baja = True
            print(f"El técnico {self.nombre} se ha dado de baja.")
            
    def reincorporarbaja(self):
        if not self.baja:
            print("El técnico no está de baja")
        else:
            self.baja = False
            print(f"El técnico {self.nombre} se ha reincorporado de la baja")

    def ascender(self):
        if self.cargo == 2:
            print("El técnico ya tiene el cargo máximo (2)")
        else:
            self.cargo += 1
            print(f"El técnico {self.nombre} ha ascendido al cargo {self.cargo}")

    def asignarespecialidad(self, especialidad):
        if especialidad in self.especialidad:
            print(f"El técnico ya tiene la especialidad {especialidad}")
        else:
            self.especialidad.append(especialidad)
            print(f"Se ha añadido la especialidad {especialidad} al técnico {self.nombre}")

    def quitarespecialidad(self, especialidad):
        if especialidad not in self.especialidad:
            print(f"La especialidad {especialidad} no está en la lista del técnico {self.nombre}")
        else:
            self.especialidad.remove(especialidad)
            print(f"Se ha quitado la especialidad {especialidad} del técnico {self.nombre}")

class Reparacion:

    contadorreparaciones = 0

    def __init__(self, coche, fecha_entrada, listado_averias):
        Reparacion.contadorreparaciones += 1
        self.identificador = Reparacion.contadorreparaciones
        self.coche = coche
        self.estado = 0
        self.tipos_reparaciones = []
        for averia in listado_averias:
            self.tipos_reparaciones.append({"tipo": averia, "hecho": False})
        self.precio = 0
        self.fecha_entrada = fecha_entrada
        self.fecha_inicio = ""
        self.fecha_fin = ""
        self.presupuesto_aceptado = False

    def get_identificador(self):
        return self.identificador

    def get_coche(self):
        return self.coche

    def set_coche(self, coche):
        self.coche = coche

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        if 0 <= estado <= 4:
            self.estado = estado
        else:
            print(f"El estado {estado} no es válido para la reparación {self.identificador}")

    def get_tipos_reparaciones(self):
        return self.tipos_reparaciones

    def set_tipos_reparaciones(self, tipos_reparaciones):
        self.tipos_reparaciones = tipos_reparaciones

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_presupuesto_aceptado(self):
        return self.presupuesto_aceptado

    def set_presupuesto_aceptado(self, aceptado):
        self.presupuesto_aceptado = aceptado

    def get_fecha_entrada(self):
        return self.fecha_entrada

    def set_fecha_entrada(self, fecha):
        if self.fecha_inicio and fecha > self.fecha_inicio:
            print(f"Error en reparación {self.identificador}: La fecha de entrada no puede ser posterior a la de inicio")
        else:
            self.fecha_entrada = fecha

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def set_fecha_inicio(self, fecha):
        if fecha < self.fecha_entrada:
            print(f"Error en reparación {self.identificador}: La fecha de inicio no puede ser anterior a la de entrada")
        elif self.fecha_fin and fecha > self.fecha_fin:
             print(f"Error en reparación {self.identificador}: La fecha de inicio no puede ser posterior a la de fin")
        else:
            self.fecha_inicio = fecha

    def get_fecha_fin(self):
        return self.fecha_fin

    def set_fecha_fin(self, fecha):
        if not self.fecha_inicio:
             print(f"Error en reparación {self.identificador}: No se puede finalizar una reparación sin fecha de inicio")
        elif fecha < self.fecha_inicio:
            print(f"Error en reparación {self.identificador}: La fecha de fin no puede ser anterior a la de inicio")
        else:
            self.fecha_fin = fecha

    def __str__(self):
        return f"ID: {self.identificador}, Coche: {self.coche.marca} {self.coche.modelo}, Estado: {self.estado}, Precio: {self.precio}, Presupuesto: {self.presupuesto_aceptado}, Fechas: {self.fecha_entrada}/{self.fecha_inicio}/{self.fecha_fin}, Tareas: {self.tipos_reparaciones}"
    
    def cambiarestado(self, nuevo_estado):
        if self.estado == 0 and nuevo_estado > 0 and not self.presupuesto_aceptado:
            print(f"Error en reparación {self.identificador}: No se puede cambiar estado sin presupuesto aceptado")
        else:
            self.estado = nuevo_estado
            print(f"La reparación {self.identificador} ha cambiado al estado {self.estado}")


    def consultatiporeparaciones(self):
        print(f"Lista de reparaciones para el coche {self.coche.marca} {self.coche.modelo}:")
        for tarea in self.tipos_reparaciones:
            estado_tarea = "Hecho" if tarea["hecho"] else "Pendiente"
            print(f"- {tarea['tipo']}: {estado_tarea}")

    def aceptarpresupuesto(self):
        self.presupuesto_aceptado = True
        self.estado = 1
        print(f"Presupuesto aceptado en reparación {self.identificador} y estado cambiado a Pdte. Reparación")

    def iniciareparacion(self, fecha_inicio):
        if not self.fecha_entrada:
            print(f"Error en reparación {self.identificador}: No se puede iniciar si no hay fecha de entrada")
        else:
            self.fecha_inicio = fecha_inicio
            self.estado = 2
            print(f"Reparación {self.identificador} iniciada el {fecha_inicio} y estado cambiado a En reparación")

    def finalizareparacion(self, fecha_fin):
        if not self.fecha_inicio:
            print(f"Error en reparación {self.identificador}: No se puede finalizar si no hay fecha de inicio")
        else:
            self.fecha_fin = fecha_fin
            print(f"Reparación {self.identificador} finalizada el {fecha_fin}")

    def finalizatiporeparacion(self, tipo):
        encontrado = False
        for tarea in self.tipos_reparaciones:
            if tarea["tipo"] == tipo:
                tarea["hecho"] = True
                encontrado = True
                print(f"Se ha finalizado la tarea {tipo} en la reparación {self.identificador}")
                break
        
        if not encontrado:
            print(f"No se ha encontrado la tarea {tipo} en la reparación {self.identificador}")
        else:
            todas_hechas = True
            for tarea in self.tipos_reparaciones:
                if not tarea["hecho"]:
                    todas_hechas = False
                    break
            
            if todas_hechas:
                self.estado = 3
                print(f"Todas las tareas completadas. La reparación {self.identificador} pasa a estado Reparado") 

class Taller: 

    def __init__(self, nombre, propietario, cif):
        self.nombre = nombre
        self.propietario = propietario
        self.cif = cif
        self.lista_tecnicos = []
        self.reparaciones_presupuesto = []
        self.reparaciones_pdte_reparacion = []
        self.reparaciones_en_reparacion = []
        self.reparaciones_reparado = []
        self.reparaciones_cobrado = []
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_propietario(self):
        return self.propietario

    def set_propietario(self, propietario):
        self.propietario = propietario

    def get_cif(self):
        return self.cif

    def set_cif(self, cif):
        self.cif = cif

    def get_lista_tecnicos(self):
        return self.lista_tecnicos

    def set_lista_tecnicos(self, lista_tecnicos):
        self.lista_tecnicos = lista_tecnicos

    def get_reparaciones_presupuesto(self):
        return self.reparaciones_presupuesto

    def set_reparaciones_presupuesto(self, reparaciones):
        self.reparaciones_presupuesto = reparaciones

    def get_reparaciones_pdte_reparacion(self):
        return self.reparaciones_pdte_reparacion

    def set_reparaciones_pdte_reparacion(self, reparaciones):
        self.reparaciones_pdte_reparacion = reparaciones

    def get_reparaciones_en_reparacion(self):
        return self.reparaciones_en_reparacion

    def set_reparaciones_en_reparacion(self, reparaciones):
        self.reparaciones_en_reparacion = reparaciones

    def get_reparaciones_reparado(self):
        return self.reparaciones_reparado

    def set_reparaciones_reparado(self, reparaciones):
        self.reparaciones_reparado = reparaciones

    def get_reparaciones_cobrado(self):
        return self.reparaciones_cobrado

    def set_reparaciones_cobrado(self, reparaciones):
        self.reparaciones_cobrado = reparaciones

    def __str__(self):
        return f"Taller: {self.nombre}, Propietario: {self.propietario}, CIF: {self.cif}, Técnicos: {len(self.lista_tecnicos)}, Pdte. Presupuesto: {len(self.reparaciones_presupuesto)}, Pdte. Reparación: {len(self.reparaciones_pdte_reparacion)}, En Reparación: {len(self.reparaciones_en_reparacion)}, Reparados: {len(self.reparaciones_reparado)}, Cobrados: {len(self.reparaciones_cobrado)}"
        
    def consultanumeropdtepresupuesto(self):
        return len(self.reparaciones_presupuesto)

    def consultanumeropdtereparación(self):
        return len(self.reparaciones_pdte_reparacion)

    def consultanumeroenreparacion(self):
        return len(self.reparaciones_en_reparacion)

    def consultanumeroreparado(self):
        return len(self.reparaciones_reparado)

    def consultanumerocobrado(self):
        return len(self.reparaciones_cobrado)
    
    def informeestadotaller(self):
        print(f"--- INFORME DE ESTADO DEL TALLER: {self.nombre} ---")
        print(f"Técnicos Disponibles: {len(self.lista_tecnicos)}")
        print(f"Reparaciones Pdte. Presupuesto: {self.consultanumeropdtepresupuesto()}")
        print(f"Reparaciones Pdte. Reparación: {self.consultanumeropdtereparación()}")
        print(f"Reparaciones En Reparación: {self.consultanumeroenreparacion()}")
        print(f"Reparaciones Reparado: {self.consultanumeroreparado()}")
        print(f"Reparaciones Cobrado: {self.consultanumerocobrado()}")
    
    def listapdtepresupuesto(self):
            print(f"--- Lista Pdte. Presupuesto ({self.consultanumeropdtepresupuesto()}) ---")
            for r in self.reparaciones_presupuesto:
                print(r)

    def listapdtereparación(self):
        print(f"--- Lista Pdte. Reparación ({self.consultanumeropdtereparación()}) ---")
        for r in self.reparaciones_pdte_reparacion:
            print(r)

    def listaenreparacion(self):
        print(f"--- Lista En Reparación ({self.consultanumeroenreparacion()}) ---")
        for r in self.reparaciones_en_reparacion:
            print(r)

    def listareparado(self):
        print(f"--- Lista Reparado ({self.consultanumeroreparado()}) ---")
        for r in self.reparaciones_reparado:
            print(r)

    def listacobrado(self):
        print(f"--- Lista Cobrado ({self.consultanumerocobrado()}) ---")
        for r in self.reparaciones_cobrado:
            print(r)
    
    def crearreparacionnueva(self):
        print("--- Datos del Coche ---")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        
        c = Coche(color, marca, modelo)
        
        print("--- Datos de la Reparación ---")
        fecha = input("Fecha de entrada: ")
        averia = input("¿Qué avería tiene el coche?: ")
        
        lista_averias = [averia]
        
        r = Reparacion(c, fecha, lista_averias)
        
        self.reparaciones_presupuesto.append(r)
        
        print(f"Reparación {r.identificador} creada para el coche {marca} e insertada en Pdte. Presupuesto")


    def aceptapresupuesto(self):
        id_buscado = int(input("ID de reparación: "))
        precio_nuevo = float(input("Precio: "))
        
        rep = None
        for r in self.reparaciones_presupuesto:
            if r.get_identificador() == id_buscado:
                rep = r
        
        if rep == None:
            print(f"No existe la reparación {id_buscado} en pendientes")
            return

        tec = None
        for t in self.lista_tecnicos:
            if t.get_cargo() == 2 and not t.get_vacaciones() and not t.get_baja():
                tec = t
        
        if tec == None:
            print(f"No hay oficiales de segunda libres para la reparación {id_buscado}")
            return

        rep.set_precio(precio_nuevo)
        rep.aceptarpresupuesto()
        
        self.reparaciones_presupuesto.remove(rep)
        
        paquete = {"reparacion": rep, "tecnico": tec}
        self.reparaciones_pdte_reparacion.append(paquete)
        
        print(f"Presupuesto aceptado para {id_buscado} y asignada a {tec.get_nombre()}")

    def comienzareparacion(self):
            id_buscado = int(input("ID reparación: "))
            tipo = input("Tarea realizada: ")

            item = None
            for i in self.reparaciones_pdte_reparacion:
                if i["reparacion"].get_identificador() == id_buscado:
                    item = i
            
            if not item:
                print(f"No existe la reparación {id_buscado}")
                return

            item["reparacion"].finalizatiporeparacion(tipo)

            tarea_pendiente = None
            for t in item["reparacion"].get_tipos_reparaciones():
                if not t["hecho"]:
                    tarea_pendiente = t["tipo"]
                    break

            if tarea_pendiente:
                if tarea_pendiente not in item["tecnico"].get_tipos_reparaciones():
                    for t in self.lista_tecnicos:
                        if tarea_pendiente in t.get_tipos_reparaciones() and not t.get_vacaciones() and not t.get_baja():
                            item["tecnico"] = t
                            print(f"Nuevo técnico {t.get_nombre()} para {tarea_pendiente}")
                            break
            else:
                self.reparaciones_reparado.append(item["reparacion"])
                self.reparaciones_pdte_reparacion.remove(item)
                print(f"Reparación {id_buscado} terminada")
        
    
    def finalizareparacion(self):
        id_buscado = int(input("Introduce el ID de la reparación: "))
        
        item_encontrado = None
        for item in self.reparaciones_en_reparacion:
            if item["reparacion"].get_identificador() == id_buscado:
                item_encontrado = item
                break
        
        if item_encontrado:
            rep = item_encontrado["reparacion"]
            listo = True
            
            for tarea in rep.get_tipos_reparaciones():
                if not tarea["hecho"]:
                    listo = False
                    break
            
            if listo:
                rep.set_estado(3)
                self.reparaciones_reparado.append(rep)
                self.reparaciones_en_reparacion.remove(item_encontrado)
                print("Reparación finalizada con éxito")
            else:
                print("Error: Aún hay tareas sin terminar")
        else:
            print("La reparación no existe o no está en proceso")
        
    def cobrareparacion(self):
        id_buscado = int(input("Introduce el ID de la reparación a cobrar: "))
        
        rep_encontrada = None
        for r in self.reparaciones_reparado:
            if r.get_identificador() == id_buscado:
                rep_encontrada = r
                break
                
        if rep_encontrada:
            rep_encontrada.set_estado(4)
            self.reparaciones_cobrado.append(rep_encontrada)
            self.reparaciones_reparado.remove(rep_encontrada)
            print(f"Reparación {id_buscado} cobrada y movida a la lista de Cobrado")
        else:
            print("Error: La reparación no existe o aún no está terminada")
    

def menu_taller():
    kirritaller = Taller("Talleres Kirri", "José Manuel Jiménez", "52075116B")
    
    while True:
        print("\n" + "======================================")
        print(f"🛠️  SISTEMA DE GESTIÓN: {kirritaller.nombre}")
        print("======================================")
        print("1. Registrar Técnicos")
        print("2. Crear Nueva Reparación (Entrada de coche)")
        print("3. Aceptar Presupuesto (Asignar a Oficial)")
        print("4. Avanzar Tareas/Finalizar Reparación")
        print("5. Cobrar Reparación (Cerrar)")
        print("6. Consultar Listas de Reparaciones")
        print("7. Ver Informe de Estado")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del técnico: ")
            print("Cargos: 0: Aprendiz, 1: Especialista, 2: Oficial")
            cargo = int(input("Cargo (0-2): "))
            especialidad = input("Especialidad principal: ")
            
            t = Tecnico(nombre, cargo, [especialidad])
            t.set_tipos_reparaciones(["Frenos", "Motor", "Aceite", "Electricidad"])
            kirritaller.lista_tecnicos.append(t)
            print(f"✅ Técnico {nombre} registrado correctamente.")

        elif opcion == "2":
            kirritaller.crearreparacionnueva()

        elif opcion == "3":

            kirritaller.listapdtepresupuesto()
            if kirritaller.consultanumeropdtepresupuesto() > 0:
                kirritaller.aceptapresupuesto()
            else:
                print("No hay reparaciones esperando presupuesto.")

        elif opcion == "4":
            kirritaller.listapdtereparación()
            if kirritaller.consultanumeropdtereparación() > 0:
                kirritaller.comienzareparacion()
            else:
                print("No hay reparaciones pendientes de iniciar.")

        elif opcion == "5":
            kirritaller.listareparado()
            if kirritaller.consultanumeroreparado() > 0:
                kirritaller.cobrareparacion()
            else:
                print("No hay reparaciones terminadas para cobrar.")

        elif opcion == "6":
            print("\n--- CONSULTA DE LISTAS ---")
            print("1. Pendientes Presupuesto\n2. Pendientes Reparación\n3. Reparados\n4. Cobrados")
            sub = input("Elija lista: ")
            if sub == "1": kirritaller.listapdtepresupuesto()
            elif sub == "2": kirritaller.listapdtereparación()
            elif sub == "3": kirritaller.listareparado()
            elif sub == "4": kirritaller.listacobrado()

        elif opcion == "7":
            kirritaller.informeestadotaller()

        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("⚠️ Introduce una opción válida")

def principal():

    #LLamada al constructor
    c1 = Coche('rojo', 'Peugeot', '307')

    #Mostramos el valor de un atributo
    print("Color de c1: " + c1.color)

    # Mostramos el valor del atributo de clase
    print("El número de coches actual es: " + str(c1.contadorcoches))

    #Imprimimos la clase. No tiene definido el método de impresión, __str__????
    print(str(c1))

    # LLamada al constructor
    c2 = Coche('azul', 'Ford', 'Fiesta')

    print("Color de c2: " + c2.color)

    print("El número de coches actual es: " + str(c2.contadorcoches))

    #Imprimimos el valor del atributo de clase, sin hacer uso de una instancia, sino del nombre de la clase
    print("El número de coches actual es: " + str(Coche.contadorcoches))

    #LLamadas a métodos
    c1.acelerar(20)

    print("Velocidad de c1: " + str(c1.velocidad))

    c1.acelerar(30)

    print("Velocidad de c1: " + str(c1.velocidad))

    #Otra forma de llamar a los métodos
    #Se utiliza el método como una función de la clase, y se le pasa un objto y los atributos
    Coche.acelerar(c1, 60)

    print("Velocidad de c1: " +str(c1.velocidad))

    c2.acelerar(100)

    print("Velocidad de c2: " + str(c2.velocidad))

    Coche.frenar(c2,20)

    print("Velocidad de c2: " + str(c2.velocidad))

    c3=Cochemarchas(6,'azul', 'Wolkswagen', 'Passat cc')

    print("El número de marchas de c3 es: " + str(c3.marchas))

    print(type(c1))
    print(type(c2))
    print(type(c3))

    print("c1 es instancia de Coche?: " + str(isinstance(c1,Coche)))
    print("c1 es instancia de Cochemarchas?: " + str(isinstance(c1, Cochemarchas)))

    print("c3 es instancia de Coche?: " + str(isinstance(c3, Coche)))
    print("c3 es instancia de Cochemarchas?: " + str(isinstance(c3, Cochemarchas)))

    print("Clase Coche es subclase de Cochemarchas: " + str(issubclass(Coche,Cochemarchas)))

    print("Clase Cochemarchas es subclase de Coche: " + str(issubclass(Cochemarchas,Coche)))

    print(f"Contador antes de crear el Audi: {Coche.contadorcoches}")       

    a1 = Cochemarchas(5, 'rojo', 'Audi', 'A1')
    
    print(f"Coche: {a1.marca} {a1.modelo} - Marchas: {a1.marchas}")
    a1.acelerar(80)
    print(f"Velocidad actual: {a1.get_velocidad()}")
    
    print(f"Contador después de crear el Audi: {Coche.contadorcoches}")  
    
    print("\nPrueba básica:")
    a1.quitarfrenomano()
    a1.cambiomarcha(1)
    a1.rugir()
    
    print("\nPrueba de calado")
    a1.set_velocidad(10)
    a1.cambiomarcha(5) # Esto tiene que calar el coche
    
    print("\nPrueba de revoluciones (le ponemos mucha velocidad con una marcha baja)")
    a1.set_velocidad(100)
    a1.cambiomarcha(2)
    
    print("\nPrueba de marcha atrás")
    a1.set_velocidad(5)
    a1.cambiomarcha(-1) # Como se está moviendo dará error
    
    print("\nPrueba de freno de mano y punto muerto")
    a1.set_velocidad = 0
    a1.ponerpuntomuerto()
    a1.rugir()
    a1.cambiomarcha(-1) # Ahora si deja poner la marcha atrás
    a1.ponerfrenomano()
    
    tesla = Cocheautomatico('blanco', 'Tesla', 'Model 3')
    print(f"Coche automático: {tesla.marca} {tesla.modelo}")
    
    # Muestro el modo actual y llamo a rugir()
    print(f"Modo actual: {tesla.modo}")
    tesla.rugir() 
    
    # Cambio a Drive y lalamo a acelar()
    tesla.cambiarmodo('D')
    tesla.acelerar(50) # Acelerar va a llamar a rugir()
    
    # Pongo la reversa
    tesla.cambiarmodo('R')
    tesla.rugir() # Tiene que sonar el pi... pi.. pi.....
    
    # Prueba de error
    tesla.cambiarmodo('X') 
    
    garaje = []

 
    garaje.append(c1)  
    garaje.append(a1)   
    garaje.append(tesla) 


    ferrari = Cochemarchas(6, 'Rojo', 'Ferrari', 'F40')
    ferrari.cambiomarcha(1) # 
    garaje.append(ferrari)


    for vehiculo in garaje:
        print(f"\nSonido del {vehiculo.get_marca()} {vehiculo.get_modelo()}:")
        vehiculo.rugir()

    
#Punto de entrada a la ejecución del programa en Python
if __name__ == '__main__':

    menu_taller()