def es_multiplo(numero_a: float, numero_b: float) -> bool:
    check_multipo = numero_a % numero_b == 0
    return check_multipo

def es_primo(numero_a_verificar: float) -> bool:
    """_summary_
    VERIFICA SI EL NUMERO ES PRIMO O NO (MAS DESARROLLADA).
    Args:
        numero_a_verificar (float): _description_ 

    Returns:
        bool: _description_
    """
    if numero_a_verificar < 2:
        return False

    contador_divisores = 2
    contador_numerico = 2
    while contador_numerico < numero_a_verificar:
        if es_multiplo(numero_a_verificar,contador_numerico):
            contador_divisores += 1
            break
        contador_numerico += 1
    validar_es_primo = contador_divisores == 2
    return validar_es_primo

def mostrar_numeros_primos_hasta(numero_tope_a_verificar: int) -> None:

    for numero in range(0,numero_tope_a_verificar + 1):
        if es_primo(numero):
            texto = f'El numero {numero} ES PRIMO'
            
        else:
            texto = f'El numero {numero} NO ES PRIMO'
        print(texto)