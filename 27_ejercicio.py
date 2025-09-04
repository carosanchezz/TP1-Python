#27.Estadísticas de ventas con arrays:
#Consigna: Escribe una función que reciba un array con las ventas de cada mes y devuelva un diccionario con el total de ventas, el promedio mensual, y el mes con mayores ventas.
#ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]


ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def estadisticas_ventas(ventas):
    total = sum(ventas)
    promedio = round(total / len(ventas), 2)
    maximo = max(ventas)
    mayor_mes = ventas.index(maximo) + 1

    return {
        "TOTAL VENTAS ": total,
        "PROMEDIO ": promedio,
        "MES DE MAYOR VENTA ": mayor_mes,
        "LA MAYOR VENTA FUE DE ": maximo
    }
estadisticas = estadisticas_ventas(ventas_mensuales)

for clave, valor in estadisticas.items():
    print(f"{clave}: {valor}")

