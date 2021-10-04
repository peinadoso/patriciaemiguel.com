#Ingrese 1 caracter por vez. hasta que se ingrese un string que no tenga longitud 1,
#o cuando el string ingresado sea un cero. Mostrar el string completo que se formó y
#qué porcentaje de caracteres del total fueron la letra “a”.


cadena = ''
contador = 0
while True:
    caracter = input('Ingrese un caracter: ')
    
    if caracter == '0' or len(caracter) > 1:
        break
    
    if caracter == 'a' or caracter == 'A':
        contador += 1
    
    #Formado de cadena de caracteres ingresados    
    cadena = cadena + caracter

print(f'Se ingresaron {contador} ases')
porcentaje = (contador/len(cadena))*100
print('La cadena formada es:', cadena,'\r\nEl procentaje de aparicion de la "a" o "A" es de:', int(porcentaje),'%')


