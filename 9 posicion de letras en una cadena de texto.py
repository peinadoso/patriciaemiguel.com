# Escribe un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. 
# A continuación, mostrar en pantalla la primera letra del texto ingresado. 
# Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres
# que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número
# entre 0 y 4) y almacenar este número en una variable llamada indice. 
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.
 
def procesamiento(texto, num):
    primera_letra = texto[:1] # Se consulta el rango del inicio del texto a la sieguiente posicion
    indice = texto[num-1:num] # num-1 porque la primera posicion es 0, el indice dado es la posicion de la letra
    print(f'La primera letra del texto es: {primera_letra}')
    print(f'La letra de la posicion {num} es {indice}')

escrito = input('Ingrese un texto aqui: ')
posicion = int(input(f'Ingrese un numero menor a {len(escrito)} para saber que letra esta en esa posición: '))

procesamiento(escrito, posicion)


