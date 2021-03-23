import random
def adivinar(intentos):
    print('Tiene {0} oportunidades para adivinar un número entero entre 0 y 100'.format(intentos))
    numero = random.randint(0, 100)
    #Se imprime el número para conocerlo y testear el programa.
    #print(str(numero))
    i=0
    while(i<intentos):
        x=int(input('Intentos restantes: {0}. Ingrese un número entero entre 0 y 100: '.format(intentos-i)))
        if x == numero:
            print('Felicitaciones, usted ha acertado en el intento nro', str(i+1), '!')
            break
        elif i<(intentos-1):
            print('Vuelva a intentar')
            i=i+1
        else:
            i=i+1
    else:
        print('Número de intentos superado, no ha logrado adivinar el número.')

adivinar(5)