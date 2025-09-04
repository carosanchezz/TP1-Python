#31.Gestión de una red social con **kwargs y arrays:
#Consigna: Escribe una función que administre publicaciones de una red social. La función debe recibir el nombre del usuario, el texto de la publicación y un número variable de etiquetas usando **kwargs y arrays. Además, debe manejar opciones adicionales como visibilidad pública o privada. La función debe devolver un diccionario con todos los detalles de la publicación.
#publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)

def publicar(usuario, texto, etiquetas=None, **kwargs):
    if etiquetas is None:
        etiquetas=[]

    publicacion = {
        "Usuario": usuario,
        "Texto": texto,
        "Etiquetas": etiquetas
    }

    for clave, valor in kwargs.items():
        publicacion[clave] = valor

    return publicacion

posteo = publicar(
    "Juan",
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"],
    visibilidad="publica", likes=100
)

for clave, valor in posteo.items(): print(f"{clave}: {valor}")
