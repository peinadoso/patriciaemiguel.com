#Muestre la sumatoria de todos los números entre el 0 y el 100.

def sumatoria():
    suma = 0
    
    for i in range(101):
        suma = suma + i
        print(f'{i} + {suma} = {suma+i}')
    return suma 

resultado = sumatoria()

print(resultado)