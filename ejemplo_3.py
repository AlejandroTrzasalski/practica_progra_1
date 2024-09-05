# 1 - Crear una funcion sin parámetros que imprima 'Bienvenidos a la UTN'
def bienvenida() -> None:
    """_summary_
    La funcion imprime con el mensaje 'Bienvenidos a la UTN'
    """
    print('Bienvenidos a la UTN')

# 4 - Crear una función que dado una base y una altura, calcule y retornar el area 
# de un rectángulo

def calcular_area_rectangulo(base: float, altura: float) -> float:
    area = (base * altura)
    print(f'El rectángulo de base {base} y altura {altura} tiene un area de {area}')
    return area

# 6 - Crear una funcion con parámetros que dado dos numeros, retorne True si son multiplos, 
# False caso contrario
def es_multiplo(numero_a: int, numero_b: int) -> bool:
    """_summary_

    Args:
        numero_a (int): _description_
        numero_b (int): _description_

    Returns:
        bool: _description_
    """
    check_multiplo = numero_a % numero_b == 0
    return check_multiplo

# 7 - Crear una funcion con parámetros que dado un numero, retorne si el numero es primo o no.
def validar_si_es_primo(numero_a_verificar_primalidad: int) -> bool:
    """_summary_

    Args:
        numero_a_verificar_primalidad (int): _description_

    Returns:
        bool: _description_
    """
    # Arrancamos con que es divisible por si mismo y por 1, con lo cual
    # Decimos que tiene al menos dos divisores
    if numero_a_verificar_primalidad < 2:
        return False
    
    contador_divisores = 2
    posible_divisor = 2
    while posible_divisor < numero_a_verificar_primalidad:
        if es_multiplo(numero_a_verificar_primalidad, posible_divisor):
            contador_divisores += 1
            # si encontramos un tercer divisor lo sumamos al contador
            # y cortamos el bucle
            break
        posible_divisor += 1
    # Si tiene mas de 2 divisores, no es un numero primo
    es_primo = contador_divisores == 2
    return es_primo


# 8 - Crear una funcion con parámetros que dado un numero, recorra todos los numeros anteriores y diga
#       cual de ellos es numero primo y cuales no lo es.

def mostrar_numeros_primos_hasta(numero_tope_a_verificar_primalidad: int) -> None:
    """_summary_

    Args:
        numero_tope_a_verificar_primalidad (int): _description_
    """
    for numero in range(0, numero_tope_a_verificar_primalidad + 1):
        if validar_si_es_primo(numero):
            texto = f'El número {numero} ES PRIMO'
        else:
            texto = f'El número {numero} NO ES PRIMO'
        print(texto)

# bienvenida()
# calcular_area_rectangulo(15, 4)
# calcular_area_rectangulo(altura=4, base=15)
# print(es_multiplo(15,4))

# mostrar_numeros_primos_hasta(1100)

# 10 - Crear una funcion con parametros, que dada una palabra, cuente la cantidad total
#      de letras y retorne dicha cantidad como entero. 

def contar_letras_texto(texto: str) -> int:
    contador_caracteres = 0
    for catacter in texto:
        contador_caracteres += 1
    print(contador_caracteres)
    return contar_letras_texto

# 11 - Crear una funcion sin parametros que pida al ausuario que ingrese tres palabras,
#       calculará cual de ellas tiene la mayor cantidad de caracteres y tendra que imprimirla
#       junto con la cantidad de letras que posee.

def ingresar_palabras():

    cantidad_de_caracteres_mayor = None
    palabra_mas_larga = None

    for i in range(3):

        palabra = input(f"Ingrese la {i + 1}º palabra: ")

        cantidad_letras_palabras_actual = contar_letras_texto(palabra)
        if cantidad_de_caracteres_mayor == None or\
            cantidad_letras_palabras_actual > cantidad_de_caracteres_mayor:
                
                cantidad_de_caracteres_mayor = cantidad_letras_palabras_actual
                palabra_mas_larga = palabra

    texto = f'La palabra con mas cantidad de letras es: {palabra_mas_larga} y '\
            f'tiene un total de {cantidad_de_caracteres_mayor} caracteres'

    print(texto)

#ingresar_palabras()

if __name__ == "__main__":
    bienvenida()
    print(f"La base del rectangulo es: {calcular_area_rectangulo(15,4)}")
    print(f"La base del rectangulo es: {calcular_area_rectangulo(altura=15,base=4)}")#datos al reves
    print(es_multiplo(16,4))
    print(validar_si_es_primo(7))
    mostrar_numeros_primos_hasta(29)