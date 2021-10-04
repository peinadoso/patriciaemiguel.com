#Dado un digito por el usuario, muestre la suma de todos sus dígitos.

cadena = ''
sumatoria = 0
while True:
    num = input('Ingrese un numero: ')

    if len(num) > 1:
        print('Debe ingresar solo un numero')
        continue
    
    if num == '0':
        break

    cadena = cadena + num
    
    try:
        num = int(num)
    except:
        print('Debe ingresar solo numeros')
        continue
    
    sumatoria += num
    
print('La cadena de numeros ingresados es:', cadena)
print('La suma de todos los digitos es:', sumatoria)