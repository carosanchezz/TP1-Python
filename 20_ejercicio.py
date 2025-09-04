#20.Configuración de una aplicación con **kwargs:
#Consigna: Escribe una función que reciba configuraciones opcionales para una aplicación como modo oscuro, idioma, notificaciones, etc., usando **kwargs. La función debe devolver un diccionario con las configuraciones aplicadas.
#configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)


def configurar_app(**kwargs):
    configuraciones = {}
    for clave, valor in kwargs.items():
        configuraciones[clave] = valor
    return configuraciones

configuracion = configurar_app(Modo_oscuro=True, Idioma="es", Notificaciones=False)

print("Se aplicaron las siguientes configuraciones: ")
for clave, valor in configuracion.items():
    print(f"{clave}: {valor}")
    