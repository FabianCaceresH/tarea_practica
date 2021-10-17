# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones y módulos
import random

# --------------------------------
# Aquí dentro definir la función contar



# Aquí copiar la función lista_aleatoria
# ya elaborada


# --------------------------------
def contar(lista_numeros,numero_buscado):
    cantidad = 0
    x = 0
    while x < len(lista_numeros):
        for numero in lista_numeros:
            if numero == numero_buscado:
                cantidad +=1
                
                x += 1
            else:
                x + 1 
    return cantidad
def lista_aleatoria(inicio,fin,cantidad):
    lista_nueva = [] 
    x = 0 
    while x < cantidad:
        numero = random.randrange(inicio,fin+1)
        x += 1
        lista_nueva.append(numero)
    return lista_nueva

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 0
    fin = 9
    cantidad = 5

    # Alumno: Crear la función "contar"

    # Utilice la función "lista_aleatoria"  creado antes 
    # para generar una lista de 5 números en
    # un rango de 1 a 9 inclusive

    lista_numeros = lista_aleatoria(inicio, fin, cantidad)

    # Generar una una nueva funcion que se llame "contar",
    # que cuente la cantidad de veces que un elemento pasado
    # por parámetro se repite en la lista también pasada por parámetro
    
    # Para saber cuantas veces se repiten el elemento pasado
    # en la lista pueden usar el método nativo de list "count"
    numero_buscado = 3
    # Por ejemplo creo una lista de 5 elementos
    
    # Luego quiero averiguar cuantas veces se repite el numero 3
    #cantidad_tres = contar(lista_numeros, 3)

    # Luego de crear la función invocarla en este lugar:
    # Averiguar cuantas veces se repite el numero 3

    cantidad_tres = contar(lista_numeros, numero_buscado)

    # Imprimir en pantalla "cantidad_tres" que informa
    # cuantas veces se repite el tres en la lista

    print(f"la cantidad de veces que se repitio el {numero_buscado}a fueron {cantidad_tres} veces") #

    print("terminamos")