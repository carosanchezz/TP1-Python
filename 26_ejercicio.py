#26.Registro de empleados con tuplas y **kwargs:
#Consigna: Escribe una función que reciba el nombre, edad, y salario de un empleado como parámetros obligatorios, y otros datos como dirección, número de teléfono, etc., como **kwargs. La función debe devolver un diccionario con toda la información del empleado.
#registro_empleado("Ana", 30, 3000, Direccion="Calle Falsa 123", Teléfono="123456789")

def registro_empleado(nombre, edad, salario, **kwargs):
    empleado = { 
        "Nombre": nombre,
        "Edad": edad,
        "Salario":salario
    }
    
    for clave, valor in kwargs.items():
        empleado[clave] = valor
    return empleado

empleado1 = registro_empleado("Ana", 30, 3000, Direccion="Calle Falsa 123", Telefono="123456789")
print(empleado1)
        