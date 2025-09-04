#23.Gestión de inventario con arrays:
#Consigna: Una tienda maneja su inventario de productos en un array donde cada índice representa un producto específico y su valor es la cantidad disponible. Escribe una función que reciba el array de inventario y un número de productos vendidos (otro array) y devuelva el inventario actualizado.
#inventario = [50, 30, 20, 10]
#ventas = [5, 10, 5, 2]


inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(inventario, ventas):
    inventario_actualizado = []

    for x in range(len(inventario)):
        inventario_actualizado.append(inventario[x] - ventas[x])
    return inventario_actualizado

resultado = actualizar_inventario(inventario, ventas)

print(f"El inventario actualizado es: {resultado}") 

