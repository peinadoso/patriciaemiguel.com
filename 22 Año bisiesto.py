#Saber si un año es bisiesto. Un bisiesto debe ser divisible entre 4 y no entre 100
#excepto que también sea divisible entre 400

while True:
    año = input('Ingrese un año para saber si es bisiesto: ')
    
    if año == '0000':
        print('CHAO')
        break
    try:
        año = int(año)
    except:
        print('Ingrese solo numeros')
        continue

    residuo4 = año % 4
    residuo100 = año % 100
    residuo400 = año %400

    if residuo4 == 0 and residuo100 != 0 or residuo400 == 0:
        print(f'El año {año} es bisiesto')
    else:
        print(f'El año {año} no es bisisesto')


