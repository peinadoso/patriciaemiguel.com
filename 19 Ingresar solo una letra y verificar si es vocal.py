# Solicite al usuario una sola letra y si es una vocal, muestre el mensaje “Es vocal”. 
# Si el usuario ingresó un string de más de un carácter informarle que no se puede procesar

import re

while True:
    letra = input('Ingrese un letra: ')
    vocal = re.search('[aeiouAEIOU]', letra)
    if len(letra) < 1:
        print('PROGRAMA TERMINADO')
        break
    elif len(letra) >= 2:
        print('Debe ingresar solo una letra | Intentelo nuevamente')
        continue
    else:
        #los metodos 'search' y 'match' de re devuelven 'None' si
        #no encuentran coincidencias
        if vocal is None: 
            print('No es vocal')
        else:
            print('Es una vocal')
    

