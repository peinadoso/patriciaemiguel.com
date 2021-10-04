#Pedir al usuario dos nombres separados, imprinir TRUE si los nombres de ambas personas
#comienzan con la misma letra ó si terminan con la misma letra. 

while True:
    nombre1 = input('Ingrese el primer nombre: ')
    nombre2 = input('Ingrese el segundo nombre: ')

    longitud1 = len(nombre1)
    longitud2 = len(nombre2)

    if longitud1 < 1 or longitud2 < 1:
        print('PROGRAMA TERMINADO')
        break
    
    nombre1 = nombre1.lower()
    nombre2 = nombre2.lower()

    if nombre1.startswith(nombre2[0]) or nombre1.endswith(nombre2[:longitud2-1]):
        print(1==1)
    else:
        print(1!=1)


