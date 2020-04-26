from random2 import randrange
parametro_inicial = 1
parametro_final = 30
numero_aleatorio =  randrange(parametro_inicial, parametro_final)
intentos = 1

manejador_bucle = True
print('ADIVINA EL NUMERO ENTRE {} y {}'.format(parametro_inicial, parametro_final))
print('INTENTOS: {}\n'.format(intentos))

while manejador_bucle:
    # print(numero_aleatorio)

    if(intentos != 1):
        print('INTENTOS: {}'.format(intentos))
    
    numero = input('Ingrese un numero:\n')
    numero = int(numero)
    

    if(numero == numero_aleatorio):
        print('FELICIDADES HAZ GANADO EL NUMERO ES: {}'.format(numero_aleatorio))
        print('LO HAZ CONSEGUIDO EN {} INTENTOS'.format(intentos))

        seguir = input('**Deseas seguir jugando s/n. Si presionas cualquier otro carater se tomara como si.**\n')

        if(seguir == 's'):
            manejador_bucle = True
            intentos = 1
            numero_aleatorio =  randrange(parametro_inicial, parametro_final)
            print('Vamos bro...')
            print('Numero entre {} y {}'.format(parametro_inicial, parametro_final))
            print('INTENTOS: {}'.format(intentos))

        elif (seguir == 'n'):
            manejador_bucle = False
            print('\nESPERAMOS QUE PARA LA PROXIMA TRAIGA MAS FICHAS...')
        else:
            manejador_bucle = True
            intentos = 1
            print('No haz escogido un si o no.')
            print('Numero entre {} y {}'.format(parametro_inicial, parametro_final))
            print('INTENTOS: {}'.format(intentos))

    elif (numero > numero_aleatorio):
        print('El numero que haz escogido es MAYOR al numero correcto ++++')
        intentos = intentos + 1
    elif numero < numero_aleatorio:
        print('El numero que haz escogido es MENOR al numero correcto ----')
        intentos = intentos + 1
    else:
        print('No haz ingresado un numero incorrecto.')
        intentos = intentos + 1

    
    print('\n')
        


