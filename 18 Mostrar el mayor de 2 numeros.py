# Solicite al usuario el ingreso de dos números diferentes imprima al mayor de los dos.

def mayorMenor(numero1, numero2):
    if num1 > num2:
        mayor = num1
    else:
        mayor = num2
    return mayor

while True:
    num1 = input('Indique el primer numero: ')
    num2 = input('Indique el segundo numero: ')

    if len(num1) < 1 or len(num2) < 1:
        print('PROGRAMA TERMINADO')
        break
    
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print('Debe ingresar solo numeros | Intente nuevamente')
        continue

    if num1 == num2:
        print('Ambos numeros son identicos')
        continue
    
    cualEs = mayorMenor(num1, num2)
    print(cualEs, 'Es el mayor')

