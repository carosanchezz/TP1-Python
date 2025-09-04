#35.Optimización de rutas con arrays y tuplas:
#Consigna: Una empresa de logística necesita optimizar sus rutas de entrega. Cada ruta se representa como una tupla (origen, destino, distancia). Escribe una función que reciba una lista de rutas y un array con las distancias máximas permitidas para cada ruta. La función debe devolver las rutas que cumplen con las restricciones.
#rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
#distancias_max = [600, 400, 500]

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def rutas_validas(rutas, distancias_max):
    resultado = []
    for i, ruta in enumerate(rutas):
        origen, destino, distancia = ruta
        if distancia <= distancias_max[i]:
            resultado.append(ruta)
    return resultado


rutas_cumplen = rutas_validas(rutas, distancias_max)
print("Rutas que cumplen con la distancia máxima:")
for ruta in rutas_cumplen:
    print(ruta)
