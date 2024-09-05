# from funciones_auxiliares import mostrar_numeros_primos_hasta  #OPCION 1
# import funciones_auxiliares                                    #OPCION 2
#import funciones_auxiliares as aux                              #OPCION 3
from numeros.funciones_auxiliares_primo import *                               #OPCION 4
#from funciones import bienvenida, es_multiplo, es_primo         #OPCION 5
from funciones import (                                          #OPCION 6
    bienvenida, es_multiplo, es_primo                            
)
# from funciones_auxiliares import es_primo as validar_primo_desarrolada
# from funciones import es_primo as validar_primo_incompleta 

from validaciones.validaciones_input import validar_input_entero




numero_str = input('Ingrese un número para mostrar numeros primos hasta su numero ingresado:\n')
numero_int = validar_input_entero(numero_str)

# Validar ese numero

# Parsearlo a entero
numero_int = validar_input_entero(numero_str)
# validar_primo_incompleta(numero_int)
# validar_primo_desarrolada(numero_int)
# print(validar_primo_desarrolada)
# mostrar_numeros_primos_hasta(numero_int)                       #OPCION 1
# funciones_auxiliares.mostrar_numeros_primos_hasta(numero_int)  #OPCION 2
# aux.mostrar_numeros_primos_hasta(numero_int)                   #OPCION 3
mostrar_numeros_primos_hasta(numero_int)                         #OPCION 4

