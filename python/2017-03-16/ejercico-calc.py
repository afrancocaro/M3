# coding: utf-8

# Imports #

## Importem la llibreria de les funcions del sistema
import os

# Funcions #

## Sumar
def sumar(nombres):

    # Definim la variable de resultat final a 0
    resultat = 0

    # Per cada item a l'array, ho suma al resultat
    for i in nombres:

        # Sumem al resultat final el nombre actual
        resultat = resultat + i

    # Retornem el resultat
    return resultat

# Assignem el valor False a la variable 'soritr'
sortir = False

# Loop que s'executa mentres l'usuari no vol sortir
while (sortir == False):

    # Netejem la pantalla
    os.system('clear')

    # Mostrem les opcions que l'usuari pot triar
    print 'Quina operació vols dur a terme?'
    print '1- Sumar'
    print '2- Restar'
    print '3- Multiplicar'
    print '4- Dividir (decimals)'
    print '5- Dividir (residu)'
    print '6- Arrel Quadrada'
    print '99- Sortir de la calculadora'
    print

    # Esperem a que l'usuari introdueixi una opció
    operacio = input('Operació: ')

    # Si vol sumar
    if (operacio == 1):

        # Esperem a que l'usuari introdueixi el total de nombres que volem sumar
        quantitat = input('Quants nombres vols sumar? ')

        # Definim l'array dels nombres per sumar
        nombres = []

        # Definim l'string dels nombres per sumar
        nombres_string = ""

        # Loop per cada nombre que hem de sumar
        for i in range(1, (quantitat + 1)):

            # Esperem a l'usuari que introdueixi el nombre
            nombre = input("Quin és el número " + str(i) + ": ")

            # Afegim el nombre a l'array de nombres
            nombres.append(nombre)

            # Afegim el nombre a l'string de nombres
            nombres_string = nombres_string + str(nombre) + " + "


        # Esborrem l'ultim "+" de l'string nombres_string
        nombres_string = nombres_string[:-2]

        # Netejem la pantalla
        os.system('clear')

        # Cridem a la funció de sumar perquè ens sumi els nombres
        print "El resultat de " + nombres_string + " és: " + str(sumar(nombres))

        # Mostrem un espai
        print

        # Esperem a que l'usuari prémi una tecla per a continuar
        raw_input('Prém una tecla per a continuar...')

    # Si vol restar
    elif (operacio == 2):
        print 'Restar'

    # Si vol multiplicar
    elif (operacio == 3):
        print 'Multiplicar'

    # Si vol dividir en decimals
    elif (operacio == 4):
        print 'Dividir (decimals)'

    # Si vol dividir amb residu
    elif (operacio == 5):
        print 'Dividir (residu)'

    # Si vol fer una arrel quadrada
    elif (operacio == 6):
        print 'Arrel Quadrada'

    # Si vol sortir
    elif (operacio == 99):
        sortir = True

    # Si no ha introduït una opció correcta
    else:
        print 'Siusplau, introdueix una opció correcta'
        os.system('sleep 5')

# Netejem la pantalla
os.system('clear')
