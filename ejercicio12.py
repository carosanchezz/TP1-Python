#12.Gestión de inventario con tuplas:
#Consigna: Una tienda tiene un inventario de productos, cada producto tiene un nombre, precio y cantidad disponible. Representa cada producto como una tupla (nombre, precio, cantidad). Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.
#productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

productos = [
("laptop", 1200, 5),
("mouse", 25, 50),
("teclado", 100, 30)
]

def buscar_mascaro(lista_productos):
    mas_caro =lista_productos[0]

    for producto in lista_productos[1:]:
        if producto[1] > mas_caro[1]:
            mas_caro = producto

    return mas_caro
        
resultado = buscar_mascaro(productos)
print(f"El producto mas caro es {resultado[0]} y el precio es {resultado[1]}")

        