#Escribe una función que reciba como parámetro un número y retorne la suma de todos sus dígitos
#Finalmente, escribir un algoritmo que solicite al usuario ingresar varios números hasta que ingrese
#el número 100, con el cual cortará la repetición. Por cada número, mostrar la suma de sus dígitos
#para lo cual se llamará a la función sumatoriaDigitos.

def sumatoriaDigitos(numero):
    suma = 0
    for n in numero:
        suma = suma + int(n)
    
    return suma

num = 0
while num != '100':
    num = input('Ingrese un numero: ')
    resultado = sumatoriaDigitos(num)
    print(resultado)
