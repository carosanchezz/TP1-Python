#22. Planificación de viajes con tuplas y diccionarios:
#Consigna: Una agencia de viajes tiene diferentes paquetes turísticos, cada uno representado como una tupla (destino, precio, duración en días). Escribe una función que reciba una lista de estos paquetes y devuelva un diccionario con los destinos como claves y el precio total (precio por día * duración) como valor.
#paquetes = [
#    ("Paris", 200, 5),
#    ("Roma", 150, 4),
#    ("Londres", 180, 3)d
#]

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def crear_diccionario(paquetes):
    diccionario = {}
    for destino, precio, dias in paquetes:
        diccionario[destino] = precio * dias
    return diccionario
    
print(crear_diccionario(paquetes))