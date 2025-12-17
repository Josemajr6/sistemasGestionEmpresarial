from datetime import datetime

class Empleado:
    contador_empleado = 0

    def __init__(self, id_empleado, nombre, edad, cargo, salario, fecha_contratacion, correo, telefono, direccion, horario, contrato=True, fecha_salida=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = int(edad)
        self.cargo = cargo
        self.salario = float(salario)
        self.fecha_contratacion = fecha_contratacion
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.horario = horario
        self.contrato = contrato
        self.fecha_salida = fecha_salida
        Empleado.contador_empleado += 1

    def __str__(self):
        estado = "Contratado" if self.contrato else "No contratado"
        return f"ID: {self.id_empleado} | {self.nombre} | {self.edad} años | {self.cargo} | {self.salario}€ | {estado} | Salida: {self.fecha_salida}"

    def Despedir(self):
        if self.contrato:
            self.contrato = False
            self.fecha_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            pass

# eJuan = Empleado(1, "Juan", 19, "Programador", 1500, "2019-10-10", "juan@gmail.con", "+34 722 62 52 88", "Calle Murillo 3, Osuna", "L-V 8:00-15:00", True, None)

# print(eJuan)
# eJuan.despedir()
# print(eJuan)
    
    
