# 13. Escribir un programa que almacene las asignaturas de un curso (por ejemplo SGE, DI,
# AD, IPE2, …) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
# donde <asignatura> es cada una de las asignaturas de la lista.

asignaturas = [ "AD", "SGE", "DI", "PMDP", "OP" ]

textoMostrar = "Yo estudio "
for asignatura in asignaturas:
    if asignaturas.index(asignatura) != len(asignaturas) - 1:
        textoMostrar += asignatura + ", "
    else:
        textoMostrar += asignatura + "."


print(textoMostrar)