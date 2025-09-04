#2.	Crea un código que imprima en pantalla la siguiente expresión. 
#1|ABC
#2|DEF
#3|GHI

#Defino la matriz
matriz = (
    ('A','B','C'),
    ('D','E','F'),
    ('G','H','I')
)

#Itera sobre la matriz usando enumerate para el indice y la fila
for indice, fila in enumerate(matriz):
    numero_fila = indice + 1
    letras_fila = ''.join(fila)
    print(f"{numero_fila}|{letras_fila}")

