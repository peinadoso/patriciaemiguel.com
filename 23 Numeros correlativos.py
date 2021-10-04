#Solicite un número entero y muestre todos los números correlativos entre el 1 y el número ingresado

while True:
    numero = input('Ingrese un numero: ')

    if numero == 'fin':
        print('PROGRAMA TERMINADO')
        break

    try:
        numero = int(numero)
    except:
        print('Debe ingresar solo numeros')
        continue
    
    for i in range(1,numero+1):
        print(i)
    
    
    

