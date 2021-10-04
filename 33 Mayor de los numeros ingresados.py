#ingresar una cantidad de números positivos indefinida, finalizando cuando ingresa el número 0 
#informar cuál fue el mayor de los números ingresados.

numeros = list()
while True:
    num = input('Ingrese un numero: ')
    #control de ingreso de solo numeros
    try: 
        num = int(num)
    except: 
        print('Solo puede ingresar numeros')
        continue
    
    #control de salida del loop while  
    if num == 0:
        break

    #Control de ingreso de numeros solamente positivos
    if num < 0:
        print('Solo se permiten numeros positivos')
        continue

    numeros.append(num)

ordenados = sorted(numeros, reverse=True)

print('El mayor de los numeros ingresados es', ordenados[0])
