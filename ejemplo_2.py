primer_numero_original = 5
segundo_numero_original = 10

def sumar(numero_1, numero_2):
    print(hex(id(numero_1)))
    numero_1 += numero_2
    print(numero_1)
    print(hex(id(numero_1))) 
    return numero_1

print("Antes de la suma")
print(primer_numero_original)
print(hex(id(primer_numero_original)))
print("-----------------------")

sumar(primer_numero_original,segundo_numero_original)

print("-----------------------")
print("Despues de la suma")
print(primer_numero_original)
print(hex(id(primer_numero_original)))