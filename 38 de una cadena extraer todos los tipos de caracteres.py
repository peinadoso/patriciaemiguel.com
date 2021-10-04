#Solicite al usuario una cadena de caracteres (que puede contener letras, números o símbolos). 
#Analizar la cadena para mostrar: cuántas letras del abecedario (minúsculas y mayúsculas) contiene
#Cuántos símbolos (caracteres que no son ni letras ni números), cuántos dígitos numéricos 
#y de los dígitos, cuántos son múltiplos de 4.

import re

while True:
    num = input('Ingrese una cadena de caracteres cualquiera: ')

    if num == 'fin':
        print('Programa terminado')
        break
    
    #Metodo para encontrar caracteres especiales con REGEX
    specGex = re.compile('\W')
    especiales = specGex.findall(num) #El metodo 'findall' devuelve una lista
    
    if re.search('[\W]', num):
        print(len(especiales), 'Caracteres especiales encontrados') 
        print(especiales,'\r\n') 

    charGex = re.compile('[a-zA-Z]')
    letras = charGex.findall(num)
    
    if re.search('[a-zA-z]', num):
        print(len(letras), 'letras encontradas')
        print(letras,'\r\n')
    
    charNum = re.compile('[0-9]')
    numeros = charNum.findall(num)
    
    if re.search('[0-9]', num):
        print(len(numeros), 'Numeros encontrados')
        print(numeros,'\r\n')




