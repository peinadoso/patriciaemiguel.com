#Mostrar el factorial de un numero


while True: 
    num = input('Ingrese un numero: ')

    if num == '0':
        print('Chao pescao')
        break

    try:
        num = int(num)
    except:
        print('Ingrese solo numeros')
        continue
    
    factorial = 1 #Se declara en 1 porque todo numero * 0 = 0
    for i in range(1, num+1): #Rango desde 1 y hasta num+1 para que no comience a multiplicar en 0
        factorial *= i

    print(factorial)
