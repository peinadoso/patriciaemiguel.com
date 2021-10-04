#Permite al usuario ingresar números enteros. La repetición terminará cuando el usuario ingrese un
#número para el cual la suma de sus dígitos sea mayor a 1000 ó múltiplo de 5. Finalmente,
#mostrar cuántos números impares ingresó el usuario antes de cortar la repetición.

impar = 0
def impares(numero):
    global impar
    if int(numero)%2 == 0:
        print('Es par')
    else:
        impar += 1
        print('Es impar')
    return impar

def sumatoria(numeral):
    suma = 0 #Se reinicializa la variable antes del for para que no arrastre el resultado de la 
             #operacion del loop del numero anterior
    for n in num:
        suma = suma + int(n)
    return suma

#En este caso fue importante separar la variable que guarda los datos ingresados por teclado de la 
#variable que procesa esos datos como un int porque si no no se puede hacer la validacion del while
num = input('Ingrese un numero: ')
number = int(num)
while not (number > 1000 or number%5 == 0):
    #Se llama a la funcion sumatoria y se imprime el return de esa funcion
    suma = sumatoria(number)
    print(f'La sumatoria de los digitos es: {suma}')
    #Se llama a la funcion impares
    impares(num)
    #Pido nuevos datos para reiniciar el loop while
    num = input('Ingrese un numero: ')
    number = int(num)

resultado = impares(num)
print(f'Se encontraron {resultado} numeros impares')
