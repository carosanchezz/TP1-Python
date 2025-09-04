#24.Organización de eventos con *args:
#Consigna: Escribe una función que reciba un número variable de nombres de eventos y los imprima en un formato de lista numerada. Utiliza *args para recibir los nombres de los eventos.
#organizar_eventos("Concierto", "Exposición de arte", "Conferencia")

def eventos(*args):
    print("Lista de eventos:")
    for x, evento in enumerate(args, start=1):
        print(f"{x}. {evento}")

eventos("Concierto", "Exposición de Arte", "Conferencia", "Recital", "Partido")