#33.Sistema de reservas con tuplas y diccionarios:
#Consigna: Un hotel maneja sus reservas utilizando un diccionario donde la clave es la fecha y el valor es una lista de tuplas, cada tupla contiene el nombre del huésped, la habitación asignada y el precio. Escribe una función que permita hacer una nueva reserva verificando primero si la habitación está disponible en la fecha seleccionada.
#reservas = {
#    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
#    "2024-08-16": [("Luis", 101, 150)]
#}

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def reservar(reservas, fecha, nombre, habitacion, precio):
    if fecha not in reservas: 
        reservas[fecha] = []
        for _, hab, _ in reservas[fecha]:
          if hab == habitacion:
            return f"La habitación {habitacion} no está disponible el {fecha}."
    

    reservas[fecha].append((nombre, habitacion, precio))
    return f"Reserva realizada para {nombre} en la habitación {habitacion} el {fecha}."


print(reservar(reservas, "2024-08-18", "María", 103, 200))
print(reservar(reservas, "2024-08-15", "Carlos", 101, 150))  

for fecha, lista in reservas.items():
    print(f"{fecha}: {lista}")
