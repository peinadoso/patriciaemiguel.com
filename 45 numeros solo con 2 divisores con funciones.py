#Ingresa números enteros hasta que ingrese uno cuyo dígito inicial sea el 9 
#Una vez terminada la repetición, mostrar cuántos de los números que el usuario ingresó tienen sólo
#dos divisores

dosDivisores = 0
def divisores(number):
    divisor = 0
    global dosDivisores
    #Se calcula a partir de 1 porque la division entre 0 no existe y se le suma una al final del
    #rango para que pueda dividir entre el mismo numero 
    for n in range(1,number+1): 
        if number%n == 0:
            divisor += 1

    #Si el divisor es 2 entonces es numero primo, es decir, solo se divide entre el mismo numero y 1
    if divisor == 2:
        dosDivisores += 1
        print(number, 'Tiene 2 divisores')
    
    return dosDivisores

digito = input('Ingrese un numero: ')
while True:
    try:
        if digito[0] == '9':
            break
    except:
        print('Ingrese solo numeros')
        continue

    resultado = divisores(int(digito))
    digito = input('Ingrese un numero: ')

print(resultado, 'numeros tuvieron 2 divisores')