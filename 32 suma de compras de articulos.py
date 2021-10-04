#Permite al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de 
#datos que cargará) cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
#Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el monto
#total de 1000, se le debe aplicar un 10% de descuento.

suma = 0
while True: 
    compras = input('ingrese monto al detal de la compra: ')

    if compras == '0':
        break
    
    try:
        compras = int(compras)
    except: 
        print('Debe ingresar solo numeros | intente nuevamente')
        continue

    if compras < 0:
        print('Solo debe ingresar montos positivos | Intente nuevamente')
        continue

    suma = suma + compras

compras = int(compras)
total = 0
if suma > 1000:
    print(f'Se le aplicara un 10% de descuento')
    print('Sub-total:', suma)
    descuento = suma * 0.1
    print(f'10% de descuento: {descuento}')
    total = suma - descuento
    print(f'TOTAL: {total}')
else:
    print('No se aplica descuento\r\nTOTAL:', suma)

