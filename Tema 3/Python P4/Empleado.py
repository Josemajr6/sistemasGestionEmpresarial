import datetime

class Empleado ():
    contador_empleado = 0

    def __init__(self, idEmpleado, nombre, edad, cargo, salario, fecha_contratacion, correo, telefono, direccion, horario, contrato, fecha_salida):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario
        self.fecha_contratacion = fecha_contratacion
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.horario = horario
        self.contrato = contrato
        self.fecha_salida = fecha_salida
    
    def __str__(self):
        return f"{self.idEmpleado} {self.nombre} {self.edad} {self.cargo} {self.salario} {self.fecha_contratacion} {self.correo} {self.telefono} {self.direccion} {self.horario} {self.contrato} {self.fecha_salida}"
        
    def __repr__(self):
        return str(self)
        
    def despedir(e):
        if (e.contrato == True):
             e.contrato == False
             e.fecha_salida = "2025-12-1"
             print(f"{e.nombre} ha sido despedido en la fecha: {e.fecha_salida}")
        else:
            print(f"El empleado {e.nombre} ya estaba despedido")
            

# eJuan = Empleado(1, "Juan", 19, "Programador", 1500, "2019-10-10", "juan@gmail.con", "+34 722 62 52 88", "Calle Murillo 3, Osuna", "L-V 8:00-15:00", True, None)

# print(eJuan)
# eJuan.despedir()
# print(eJuan)
    
    
