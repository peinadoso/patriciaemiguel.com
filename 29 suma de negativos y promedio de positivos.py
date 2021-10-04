#Ingresa 6 numeros enteros (+ ó -). Mostrar la suma de los negativos y el promedio de los positivos

contador = 0
num = 0
numeros = list()
while contador < 6:
    num = input('Ingrese un numero entero positivo o negativo: ')
    
    numeros.append(num)
    contador += 1

    if num == '0':
        print('El cero no esta permitido en este programa | Ingrese otro numero')
        continue

    if contador >= 6:
        break

negativos = -0 #Se declara -0 para que la suma negativa sea siempre negativa
positivos = 0
i = 0
for n in numeros:
    n = int(n)
    if n < 0:
        negativos = (negativos) + (n)
        print('negativos', n)
    else:
        positivos += n
        i += 1
        print('positivos', n)

promedio = 0
promedio = positivos/i
print(f'La suma de los negativos es = {negativos}\r\nEl promedio de los positivos es {promedio}')



    
