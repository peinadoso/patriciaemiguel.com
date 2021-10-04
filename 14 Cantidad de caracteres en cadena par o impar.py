#Dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena
#es un número impar, o False si no lo es.

def parImpar(cadenita):
    print(len(cadenita))
    print(len(cadenita) % 2 == 0)
    
while True:
    cadena = input('Ingrese un texto: ')

    if len(cadena) < 1:
        print('PROGRAMA TERMINADO')
        break
    
    parImpar(cadena)



    

