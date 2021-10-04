#Dada una frase y una letra por separados, remplaza la ocurrencia de esa letra en la frase por *

frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')

nueva = ''
for i in frase:
    if i == letra:
        nueva = nueva + '*'
    else: 
        nueva += i 

print(nueva)