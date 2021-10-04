#Permita al usuario ingresar números que serán leídos como string (no como int o float) hasta que
#ingrese uno que sea múltiplo de 10 ó menor que 0 (que no será procesado). 
#Se formarán dos strings, en los cuales se concatenarán los números ingresados, según el siguiente
#criterio: en un string se concatenarán todos los números que el usuario ingrese cuya cantidad de
#dígitos sea un múltiplo de 3. En el otro, se concatenarán todos los números que contengan el dígito 0
#Si un número cumple ambas condiciones, debe concatenarse en ambos strings. 
# En cada string, después de cada número concatenado debe colocarse el carácter “-”. 
# Al finalizar, mostrar en pantalla ambos strings.

num = input('Ingrese un numero: ')
numInt = int(num)
multiplos3 = ''
digitos0 = ''
while not (numInt%10 == 0 or numInt < 0):
    for numero in num:
        if numero == '0':
            digitos0 = digitos0 + '-' + num

    if len(num)%3 == 0:
        multiplos3 = multiplos3 + '-' + num
    
    num = input('Ingrese un numero: ')
    numInt = int(num)

    
print('Caracteres multiplos de 3:',multiplos3)
print('Numeros con 0:', digitos0)
            

