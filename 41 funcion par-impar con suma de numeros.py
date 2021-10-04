#Escribir una función llamada esPar que reciba como parámetro un número y retorne True si el número
#es par ó False si es impar. Utilizar esta función en un programa que solicite al usuario el ingreso
#de 10 números y que luego muestre, por separado, la suma de los pares y la de los impares.

pares = 0
impares = 0
#Para usar variables 'globales' es decir que se usen dentro y fuera de una funcion, hay que declararlas
#fuera de la funcion y luego definirlas como global dentro de la funcion - es la manera correcta
def esPar(numero):
    global pares
    global impares
    
    if numero % 2 == 0:
        pares = pares + numero
    else:
        impares += numero 
    
    return numero%2 == 0 #Esto devuelve True o False

n = 0
while n < 10:
    num = int(input('Ingrese un numero: '))
    resultado = esPar(num)
    print(resultado)
    n += 1

#Si no se definen estas variables como globales no las puedo usar fuera de la funcion 
print(pares)
print(impares)


