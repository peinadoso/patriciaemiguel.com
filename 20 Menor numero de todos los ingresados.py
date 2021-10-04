#Solicitar al usuario diferentes números y mostrar en pantalla al menor de todos .

numeros = list()
menor = None
num = ''

while num != 'fin':
    num = input('Ingrese un numero: ')
    try:
        num = int(num)
        numeros.append(num)
    except: 
        print('Error intente de nuevo')
        continue

    if num == 'fin':
        break

print(numeros)
for numero in numeros:
    if menor is None:
        menor = numero
    else:
        if numero < menor:
            menor = numero

print('El menor de los numeros ingresados es', menor)

########################
## SOLUCION para pedir solo 3 numeros ######
########################

# if num1 < num2 and num1 < num3:
#     menor = num1
#     print('El menor numero de todos es', menor) 

# elif num2 < num1 and num2 < num3:
#     menor = num2
#     print('El menor numero de todos es', menor)
# elif num3 < num1 and num3 < num2:
#     menor = num3
#     print('El menor numero de todos es', menor)

