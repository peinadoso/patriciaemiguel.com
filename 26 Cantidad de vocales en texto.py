#Dada una frase por el usuario, muestre la cantidad de vocales (mayúsculas y minúsculas) que contiene

import re
contador = 0
vocal = list()

frase = input('Ingrese una frase: ')

for i in frase:
    if re.search('[aeiouAEIOU]', i):
        vocal.append(i)

longitud = len(vocal)
print(vocal)
print(f'Hay {longitud} vocales en el texto')