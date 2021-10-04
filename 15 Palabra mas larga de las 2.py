#Pida al usuario ingresar dos palabras y las guarde en dos variables, luego imprima True si la
#primera palabra es menor que la segunda o False si no lo es

while True:
    word1 = input('Ingrese una palabra: ')
    word2 = input('Ingrese otra palabra: ')

    if len(word1) < 1 or len(word2) < 1:
        print('PROGRAMA TERMINADO')
        break

    print(len(word1), len(word2))
    print(len(word1) < len(word2))

    