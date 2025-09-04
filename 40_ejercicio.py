#40.Análisis de rendimiento académico con diccionarios y arrays:
#Consigna: Una universidad lleva un registro de las calificaciones de los estudiantes en diferentes materias. Cada estudiante tiene un ID único y su información se almacena en un diccionario donde la clave es el ID y el valor es otro diccionario con las materias y sus respectivas calificaciones (arrays). Escribe una función que reciba este diccionario y devuelva un ranking de estudiantes basado en su promedio general.
#estudiantes = {
#    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
#    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
#    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}


estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_estudiantes(estudiantes):
    promedios = {}
    
    for id_est, materias in estudiantes.items():
        todas_notas = []
        for notas in materias.values():
            todas_notas.extend(notas)
        promedio_general = sum(todas_notas) / len(todas_notas)
        promedios[id_est] = round(promedio_general, 2)
    
    # Ordenar por promedio de mayor a menor
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    return ranking

# Ejemplo de uso
ranking = ranking_estudiantes(estudiantes)
print("Ranking de estudiantes (ID, Promedio):")
for id_est, promedio in ranking:
    print(f"ID {id_est}: {promedio}")


