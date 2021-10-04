#Ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string *. Cada vez que
#el usuario ingrese un string de longitud 1 que contenga sólo una barra “/” se considera que
#termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
#aparecieron en total (en todos los títulos de libros que componen en esa línea). 
#Finalmente, informar cuántas líneas completas se ingresaron.

import re

titulo = input('Ingrese el nombre de un libro: ')
cadena = ''
lineas = 0

while True:
    cadena += titulo
    lineas += 1

    if titulo == '*':
        break

    if titulo == '/':
        numeros = re.findall('[0-9]', cadena)
        print('Se encontraron', len(numeros), 'numeros en la cadena')

    
    titulo = input('Ingrese el nombre de un libro: ')

print('Se ingresaron', lineas, 'lineas')