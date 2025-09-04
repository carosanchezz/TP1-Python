#34.Análisis de resultados de encuestas con diccionarios y arrays:
#Consigna: Una empresa realiza encuestas de satisfacción y registra las respuestas en un diccionario donde la clave es la pregunta y el valor es un array con las respuestas recibidas. Escribe una función que calcule la frecuencia de cada respuesta para cada pregunta y devuelva un diccionario con estos resultados.
#encuestas = {
#    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
#    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
#}

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def frecuencia_respuestas(encuestas):
    resultados = {}
    for pregunta, respuesta in encuestas.items():
        frecuencia = {}
        for respuesta in respuesta:
         if respuesta in frecuencia:
            frecuencia[respuesta] += 1
         else:
            frecuencia[respuesta] = 1
        resultados[pregunta] = frecuencia
    return resultados

frecuencia = frecuencia_respuestas(encuestas)

print("Análisis de encuestas")

for pregunta, freq in frecuencia.items():
    print(f"{pregunta}:")
    for respuesta, cantidad in freq.items():
        print(f"  Respuesta {respuesta}: {cantidad}")
