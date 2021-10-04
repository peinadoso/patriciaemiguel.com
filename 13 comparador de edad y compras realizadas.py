#Solicite al usuario su edad, luego solicite la cantidad de artículos comprados en una tienda
#Finalmente, mostrar (True o False) si el usuario es mayor de 18 años y compró más de 1 artículo

while True:
    edad = input('Indique su edad: ')
    cantArt = input('Indique la cantidad de articulos que compro: ')
    
    if len(edad) < 1 or len(cantArt) < 1:
        print('PROGRAMA TERMINADO')
        break 
    
    try: 
        edad = int(edad)
        cantArt = int(cantArt)
    except: 
        print('Debe incluir solo numeros, intente nuevamente')
        continue

    if edad > 18 and cantArt > 1:
        print(edad > 18 and cantArt > 1)
    else:
        print('Es menor de edad, no puede comprar en esta tienda')
        continue



