from Empleado import Empleado

class Empresa():
    contador_empresa = 0
    def __init__(self, nombre, direccion, industria, telefono, correo, empleado):
        self.nombre = nombre
        self.direccion = direccion
        self.industria = industria
        self.telefono = telefono
        self.correo = correo
        self.empleado = empleado
    
    def __str__(self):
        return f"{self.nombre} {self.direccion} {self.industria} {self.telefono} {self.correo} {self.empleado}"
    
    def agregar_empleado(self, em):

        if isinstance(em, Empleado):
            self.empleado.append(em)
            print(f"Se ha añadido a {em.nombre} a la lista de empleados")
        else:
            print(f"El empleado {em.nombre} ya existe en la lista de empleados")

    def eliminar_empleado(self, idEmpleado):
        existe = True
        for e in self.empleado:
            if (e.idEmpleado == idEmpleado):
                existe = True
                em = e
        if (existe == True):
            self.empleado.remove(e)
            print(f"Se ha borrado a {em.nombre} de la lista de empleados")
        else:
            print(f"El empleado con ID {idEmpleado} no existe existe en la lista de empleados")

    def calcular_costo_salarial(self):
        suma = 0
        for e in self.empleado:
            suma += e.salario
        return suma
    
    def lista_empleados(self):
        for e in self.empleado:
            print(e)
    
