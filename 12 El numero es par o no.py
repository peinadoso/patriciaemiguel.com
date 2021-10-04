# Solicitar al usuario el ingreso de un número entero y que luego imprima 
# true o false dependiendo de si el número es par o no. 

def parimpar(num):
    if int(num) % 2 == 0:
        print(f'El numero {num} es par')
    else:
        print(f'El numero {num} es impar')

while True:
    numero = input('Ingrese un numero entero: ')
    try:
        parimpar(numero)
        continue
    except:
        print('Debe ingresar solo numeros')
        quit() # Esta funcion termina el programa por completo 