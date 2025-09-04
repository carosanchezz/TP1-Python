#29. Registro de notas con tuplas y arrays:
#Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante y sus calificaciones en un array. La función debe devolver un diccionario con el nombre del estudiante como clave y su promedio de calificaciones como valor.
#notas_estudiantes = [
#    ("Ana", [85, 90, 78]),
#    ("Luis", [88, 92, 80]),
#    ("María", [75, 85, 70])
#]

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def promedios_estudiantes(lista_notas):
    nota_final = {}

    for nombre, calificaciones in lista_notas:
        promedio = round(sum(calificaciones) / len(calificaciones), 2)
        nota_final[nombre] = promedio
    return nota_final

promedios = promedios_estudiantes(notas_estudiantes)
print("Los promedios de los alumnos son: ")
for nombre, nota_final in promedios.items():
    print(f"{nombre}: {nota_final}")
