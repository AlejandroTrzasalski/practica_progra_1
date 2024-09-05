import math
# Ejercicios









# 2 - Crear una funcion sin parámetros que retorne el año actual como numero entero
def año_actual() -> int:
    while True:
        año = input("Introduzca el año actual: \n")
        if año.isdigit() and int(año) >= 2024:
            return int(año)
        else:
            print("Error. El año debe ser igual o mayor a 2024. Intente nuevamente.\n")

# año = año_actual()
# print(f"El año acutal es: {año}")

# 3 - Crear una función que dado un parametro que corresponde a un nombre, salude.

def saludar_nombre(nombre: str) ->str:
    return f"Hola {nombre}, como estas?!"

# nombre_obtenido = input("Ingrese su nombre: \n")

# saludo = saludar_nombre(nombre_obtenido)
# print(saludo)


# 5 - Crear una funcion con parámetros que dado un radio, calcule el area de un circulo

def area_circulo(radio: float) -> float:
    return math.pi * radio**2

# radio_ingresado = float(input("Ingrese el radio del círculo: \n"))

# area = area_circulo(radio_ingresado)
# print(f"El área del círculo con radio {radio_ingresado} es: {area:.2f}")

# 9 - Crear una función con parametros que dada una palabra y una letra, retorne 
#       la cantidad de letras coincidentes que tiene esa palabra 

def contar_letra_coincidente(palabra:str,letra:str) ->int:
    if len(letra) != 1:
        return ("Error.\n")
    
    contador_letras = 0

    for caracter in palabra:
        if caracter == letra:
            contador_letras += 1

    return contador_letras

palabra = input("Ingrese una palabra: \n")
letra = input("Inrese el caracter que quiera contar dentro de la palabra: \n")

cantidad_de_caracteres = contar_letra_coincidente(palabra,letra)

if cantidad_de_caracteres == -1:
    print("Error.")
else:
    print(f"El caracter '{letra}' aparece {cantidad_de_caracteres} veces en la palabra {palabra}.\n")


