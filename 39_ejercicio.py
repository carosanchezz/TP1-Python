#39.Simulación de mercado bursátil con arrays y tuplas:
#Consigna: Escribe una función que simule el comportamiento de acciones en un mercado bursátil. La función debe recibir un array con los precios diarios de una acción y una lista de tuplas donde cada tupla contiene un día y un precio de compra o venta. La función debe devolver el beneficio o pérdida total si las acciones se hubieran comprado y vendido en los días especificados.
#precios_diarios = [100, 105, 102, 110, 108]
#operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simular_mercado(precios, operaciones):
    beneficio_total = 0
    accion_abierta = None 
    
    for op, dia in operaciones:
        precio = precios[dia]
        if op == "compra":
            accion_abierta = precio
        elif op == "venta":
            if accion_abierta is not None:
                beneficio_total += precio - accion_abierta
                accion_abierta = None
            else:
                print(f"Error: venta en día {dia} sin acción comprada.")
    
    return beneficio_total

resultado = simular_mercado(precios_diarios, operaciones)
print(f"Beneficio/Pérdida total: {resultado}")
