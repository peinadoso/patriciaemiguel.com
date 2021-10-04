# Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo 
# en una única variable. A continuación, mostrar el resultado final en pantalla.

def porciento(num):
    porcentuado = num - (num * 0.15)
    return porcentuado

numero = float(input('Ingrese un numero: '))
resultado = porciento(numero)
print(f"El resultado es: {resultado}")
