#16.Creación de un perfil de usuario con **kwargs:
#Consigna: Escribe una función que reciba datos de un usuario como nombre, edad, correo electrónico, y cualquier otro dato adicional usando **kwargs. La función debe devolver un diccionario con toda la información del usuario.
#Crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")

def crear_perfil(**kwargs):
    #Recibe los datos como argumento y los devuelve 
    return kwargs

perfil = crear_perfil(nombre="Luis", edad=25, email="juan@gmail.com", ciudad="Mendoza")
print(perfil)