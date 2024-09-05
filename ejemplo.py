def calcular_precio_con_iva(precio_sin_iva: float, iva=21) -> float:
    """
    Calcula el IVA de un precio, con valor
    por defecto del 21% y retorna el precio con IVA.

    Args:
        precio_sin_iva(float): _description_ El Precio del producto
        sin IVA agregado
    iva (int,optional): _description_. El IVA a sumar, por defecto
    es opcional y 21.

    Retorna el precio base con el iva agregado, para cumplir con la ley.

    """
    
    resultado = precio_sin_iva * (1 + iva/100)
    return resultado


def calcular__medio_aguinaldo(salario: float) -> float: # medio porque seria uno de los 2 aguinaldos anuales
    """Calcula medio aguinaldo en base al salario ingresado
    por parametro y lo retorna.

    Args:
        salario (float): _description_: Es el salario de la persona trabajadora
            que se usara para calcular el medio aguinaldo

    Returns:
        _type_: _description_: El aguinaldo calculado en base al salario.
    """
    
    resultado = salario / 2
    return resultado



#Toma de dato 
iva = 21
precio_sin_iva = float(input(f'Ingrese un valor para calcular el IVA {iva}%: \n$'))

# Transformacion de datos
precio_con_iva = calcular_precio_con_iva(precio_sin_iva,iva)

# Creando un output
mensaje = f'El valor con IVA del 21% de ${precio_sin_iva} es de: ${precio_con_iva}'

# Mostrando al usuario la salida
print(mensaje)





