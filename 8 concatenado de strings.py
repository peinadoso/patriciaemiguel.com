# Escribe un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán
# en dos variables distintas. A continuación, almacen en una variable la concatenación de la primera 
# palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla.

def concatenacion(word1, word2):
    resultado = word1 + ' ' + word2
    return resultado

palabra1 = input('Ingrese la primera palabra: ')
palabra2 = input('Ingrese la segunda palabra: ')

impresion = concatenacion(palabra1, palabra2)

print(impresion.capitalize())#Si las palabras insertadas se incluyeron en minusculas con el metodo capitalize se coloca la primera letra en mayuscula
