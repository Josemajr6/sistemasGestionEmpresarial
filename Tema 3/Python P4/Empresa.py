from Empleado import Empleado

class Empresa:
    contador_empresa = 0

    def __init__(self, nombre, direccion, industria, telefono, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.industria = industria
        self.telefono = telefono
        self.correo = correo
        self.empleado = []
        Empresa.contador_empresa += 1

    def __str__(self):
        return f"Empresa: {self.nombre} | {self.industria} | Empleados: {len(self.empleado)}"

    def agregar_empleado(self, nuevo_empleado):
        for e in self.empleado:
            if e.id_empleado == nuevo_empleado.id_empleado:
                print("Error: El empleado ya existe.")
                return
        self.empleado.append(nuevo_empleado)

    def eliminar_empleado(self, id_empleado):
        for e in self.empleado:
            if e.id_empleado == id_empleado:
                self.empleado.remove(e)
                return
        print("Error: No existe empleado con ese ID.")

    def calcular_costo_salarial(self):
        total = 0
        for e in self.empleado:
            if e.contrato:
                total += e.salario
        return total

    def listar_empleados(self):
        for e in self.empleado:
            print(e)