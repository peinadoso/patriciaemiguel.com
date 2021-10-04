#Solicitar al usuario números enteros positivos hasta ingresar -1. Por cada número ingresado, mostrar
#la cantidad de pares e impares que tiene ese digito. al final, mostrar cuántos múltiplos de 3 hay 

pares = 0
impares = 0
de3 = 0

num = int(input('Ingrese un numero positivo: '))
while True:
    if num == -1:
        break   
        
    if num % 3 == 0:
        de3 += 1

    #Para determinar el ultimo digito de un numero lo divido entre 10 y el residuo me arroja el ultimo
    #digito, luego hago un loop 'while' que va a repetir el proceso hasta que ya no queden digitos por 
    #calcular
    lastDigit = 0
    while num != 0:
        lastDigit = num % 10
        if lastDigit % 2 == 0:
            pares += 1
        else: 
            impares = impares + 1
        num = num//10
    
    print('Digitos pares:', pares,'\r\nDigitos impares:', impares)

    num = int(input('Ingrese un numero positivo: '))
    
    
print('Numeros multiplos de 3:', de3)    





# print('Cantidad de numeros pares:', pares,'\r\nCantidad de numeros impares: ', impares)
# print('Cantidad de multiplos de 3: ', de3)
