#28.Organización de una biblioteca con diccionarios:
#Consigna: Una biblioteca registra sus libros en un diccionario donde la clave es el título del libro y el valor es otro diccionario con la información del autor, año de publicación, y género. Escribe una función que reciba este diccionario y devuelva una lista de todos los libros publicados después del año 2000.
#biblioteca = {
#"El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
#"Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
#"El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
#}
biblioteca = {
"El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
"Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
"El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def clasificacion_libros(libros):
    libros_actualizados = []
    for titulo, info in libros.items():
        if info["año"] > 2000:
            libros_actualizados.append(titulo)
    return libros_actualizados

clasificados = clasificacion_libros(biblioteca)
print("Libros publicados después del año 2000: ", clasificados)