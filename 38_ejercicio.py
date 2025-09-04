#38.Administración de suscripciones con diccionarios, arrays, y **kwargs:
#Consigna: Escribe una función que gestione las suscripciones a un servicio en línea. La función debe recibir el nombre del usuario, el tipo de suscripción (mensual, anual), y cualquier o	tra opción adicional usando **kwargs. La función debe actualizar un diccionario que almacene el historial de suscripciones de los usuarios y devolver el estado actualizado.
#suscripciones = {
#    "Jose": ["mensual", "anual"],
#    "Ana": ["mensual"]
#}
#actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    # Si el usuario no existe, lo agregamos
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    
    # Agregamos la suscripción si no está repetida
    if suscripcion not in suscripciones[usuario]:
        suscripciones[usuario].append(suscripcion)
    
    # Creamos un diccionario para opciones adicionales si se necesitan
    if kwargs:
        suscripciones[usuario + "_opciones"] = kwargs  # opcional: separar opciones
    
    return suscripciones

# Ejemplo de uso
estado_actual = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(estado_actual)
