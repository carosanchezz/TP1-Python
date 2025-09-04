#15.Manejo de parámetros variables con *args:
#Consigna: Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio. Utiliza *args para recibir las notas.
#calcular_promedio(85, 90, 78, 92)

def calcular_promedio(*args):
    suma = sum(args)
    promedio = suma / len(args)
    return promedio

resultado = calcular_promedio(85, 90, 78, 92)

print(f"El promedio es: {resultado}")