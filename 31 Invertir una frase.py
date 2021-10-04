#Imprimir una frase de forma invertida

frase = input('Ingrese una frase: ')

nueva = '' #Declaro un string vacio donde se cronstuira la nueva frase al reves
long = len(frase)

for n in frase: #recorro todas las letras de la frase
    long = long - 1 #Determino el ultimo valor de la frase escrita
    nueva = nueva + frase[long] #Asigno cada letra leida a la nueva variable
                                #'frase[long]' va agregando el caracter leido de la ultima posicion
                                #hacia el inicio

print(nueva)


