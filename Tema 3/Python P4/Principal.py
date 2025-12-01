from Empleado import Empleado
from Empresa import Empresa

empleados_iniciales = []

empleado1 = Empleado(1, "Juan", 19, "Programador", 1500, "2019-10-10", "juan@gmail.con", "+34 722 62 52 88", "Calle Murillo 3, Osuna", "L-V 8:00-15:00", True, "None")

empresa1 = Empresa("Ecentia", "C Nervion 13, Sevilla", "Informática", "722 625 288", "ecentiaseo@gmail.com", empleados_iniciales)

empresa1.agregar_empleado(empleado1)

print(empleado1)
print(empresa1.calcular_costo_salarial())

empleado2 = Empleado(2, "Adrían", 21, "Diseñador", 1550, "2020-11-10", "adrianli@gmail.com", "632 23 23 21", "Calle Los Molares, Estepa", "L-J 10:00-14:00", True, "None")

empresa1.agregar_empleado(empleado2)

print(empresa1)

empresa1.eliminar_empleado(1)

empresa1.lista_empleados()