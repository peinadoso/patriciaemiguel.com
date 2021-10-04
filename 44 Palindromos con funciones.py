#Escribe una función que reciba un string y retorne True si es un palíndromo, False en caso contrario.
#Permitir al usuario ingresar palabras hasta que ingrese la palabra “fin” 
#(suponer que todas las palabras son en minúsculas o todas en mayúsculas, sostenida).
#Al finalizar, mostrar la cantidad de palíndromos ingresados.

cantidad = 0
def palindromox(word):
    global cantidad
    word = word.lower()
    longitud = len(word)
    cadena = ''
    for n in word:
        longitud -= 1
        cadena = cadena + word[longitud]
    
    if word == cadena:
        print(f'{word} es un palindromo')
        cantidad += 1
    else:
        print('No es un palindromo')

    return word == cadena

palabra = input('Ingrese una palabra: ')
while not palabra == 'fin':
    resultado = palindromox(palabra)
    palabra = input('Ingrese una palabra: ')

print('Se encontraron', cantidad, 'palindromos') 