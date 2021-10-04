# Solicitar al usuario ingresar una fecha formada por 8 números, donde los primeros dos representan el día, 
# los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). 
# Este dato debe guardarse en una variable con tipo int (número entero). 
# Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.

ingreso = input('Ingrese la fecha indicando solo numeros DDMMAAAA: ')

print(f'Dia: {ingreso[:2]}')
print(f'Mes: {ingreso[2:4]}') # Recordar que para los arreglos el valor "B" [A:B] no es tomado en cuenta
print(f'Año: {ingreso[4:]}')  # El valor "B" solo indica donde se detiene el cursor para identificar el rango
print(f'En formato de fecha: {ingreso[:2]} / {ingreso[2:4]} / {ingreso[4:]}')
