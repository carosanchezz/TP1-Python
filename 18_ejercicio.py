#18.Procesamiento de ventas con arrays:
#Consigna: Una tienda quiere procesar sus ventas diarias almacenadas en un array. Escribe una función que reciba el array de ventas diarias y devuelva el total de ventas y el promedio de ventas por día.
#ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def total_y_promedio_ventas(ventas_diarias):
    total = sum(ventas_diarias)
    promedio = total // len(ventas_diarias)
    return total, promedio

total, promedio = total_y_promedio_ventas(ventas_diarias)

print(f"La suma de las ventas diarias es de: {total}")
print(f"El promedio de las ventas diarias es de: {promedio}")
