# Escribe un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año
# y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False)
# que indique si el usuario ha visto más de 3 shows.


while True:
    cantidad = input('indique cuantos shows musicales ha visto en el año: ')
    
    # Para el manejo de este while la comparacion de string salir debe ir antes y ademas separado de 
    # la comparacion int < o > a 3 porque sino afecta el flujo ya que en un mismo if | elif 
    # no se puede comparar strings con numeros
    if cantidad == 'salir':
        print('Muchas gracias por participar')
        break

    if int(cantidad) > 3:
        print('Has visto mas de 3 shows')
    elif int(cantidad) == 3:
        print('Has visto 3 shows este año')
    elif int(cantidad) == 0:
        print('No has visto shows este año')
    elif int(cantidad) < 3:
        print('has visto menos de 3 shows este año')
    continue
    