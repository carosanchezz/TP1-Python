#19.Análisis de resultados deportivos con diccionarios:
#Consigna: Un club deportivo registra los resultados de sus partidos en un diccionario donde la clave es el nombre del equipo rival y el valor es una tupla con los goles anotados y recibidos. Escribe una función que calcule el total de goles anotados y recibidos en la temporada.
#resultados = {
#    "Equipo A": (3, 2),
#    "Equipo B": (1, 1),
#    "Equipo C": (4, 0)
#}

goles = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipon C": (4,0)
}

def calcular_goles(goles):
    goles_anotados = 0
    goles_recibidos = 0

    for equipo, (anotados, recibidos) in goles.items():
        goles_anotados += anotados
        goles_recibidos += recibidos
    return goles_anotados, goles_recibidos
    
anotados, recibidos = calcular_goles(goles)

print(f"Los goles anotados en la temporada fueron: {anotados}")
print(f"Los goles recibidos en la temporada fueron: {recibidos}")
    