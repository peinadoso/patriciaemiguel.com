#· Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio

def promedio(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average

numero1 =  float(input("Indique el primer numero: "))
numero2 =  float(input("Indique el segundo numero: "))
numero3 =  float(input("Indique el tercer numero: "))

resultado = promedio(numero1, numero2, numero3)
print('El promedio de los 3 numeros es:',resultado)
