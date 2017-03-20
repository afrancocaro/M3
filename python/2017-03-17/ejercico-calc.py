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

## Restar
def restar(nombres):

    # Definim la variable de resultat final al primer nombre
    resultat = nombres[0]

    # Esborrem el primer nombre perquè ja l'hem assignat a la variable resultat
    del nombres[0]

    # Per cada item a l'array, ho resta al resultat
    for i in nombres:

        # Restem al resultat final el nombre actual
        resultat = resultat - i

    # Retornem el resultat
    return resultat

## Multiplicar
def multiplicar(nombres):

    # Definim la variable de resultat final al primer nombre
    resultat = nombres[0]

    # Esborrem el primer nombre perquè ja l'hem assignat a la variable resultat
    del nombres[0]

    # Per cada item a l'array, ho multiplica al resultat
    for i in nombres:

        # Multipliquem al resultat final el nombre actual
        resultat = resultat * i

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
    print 'S- Sortir de la calculadora'
    print

    # Esperem a que l'usuari introdueixi una opció
    operacio = raw_input('Operació: ')

    # Si vol sumar
    if (operacio == '1'):

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
    elif (operacio == '2'):

        # Esperem a que l'usuari introdueixi el total de nombres que volem restar
        quantitat = input('Quants nombres vols restar? Tingues en compte de que es restaran en ordre')

        # Definim l'array dels nombres per restar
        nombres = []

        # Definim l'string dels nombres per restar
        nombres_string = ""

        # Loop per cada nombre que hem de restar
        for i in range(1, (quantitat + 1)):

            # Esperem a l'usuari que introdueixi el nombre
            nombre = input("Quin és el número " + str(i) + ": ")

            # Afegim el nombre a l'array de nombres
            nombres.append(nombre)

            # Afegim el nombre a l'string de nombres
            nombres_string = nombres_string + str(nombre) + " - "


        # Esborrem l'ultim "-" de l'string nombres_string
        nombres_string = nombres_string[:-2]

        # Netejem la pantalla
        os.system('clear')

        # Cridem a la funció de sumar perquè ens resti els nombres
        print "El resultat de " + nombres_string + " és: " + str(restar(nombres))

        # Mostrem un espai
        print

        # Esperem a que l'usuari prémi una tecla per a continuar
        raw_input('Prém una tecla per a continuar...')

    # Si vol multiplicar
    elif (operacio == '3'):

        # Esperem a que l'usuari introdueixi el total de nombres que volem multiplicar
        quantitat = input('Quants nombres vols multiplicar? ')

        # Definim l'array dels nombres per multiplicar
        nombres = []

        # Definim l'string dels nombres per multiplicar
        nombres_string = ""

        # Loop per cada nombre que hem de multiplicar
        for i in range(1, (quantitat + 1)):

            # Esperem a l'usuari que introdueixi el nombre
            nombre = input("Quin és el número " + str(i) + ": ")

            # Afegim el nombre a l'array de nombres
            nombres.append(nombre)

            # Afegim el nombre a l'string de nombres
            nombres_string = nombres_string + str(nombre) + " * "


        # Esborrem l'ultim "*" de l'string nombres_string
        nombres_string = nombres_string[:-2]

        # Netejem la pantalla
        os.system('clear')

        # Cridem a la funció de multiplicar perquè ens sumi els nombres
        print "El resultat de " + nombres_string + " és: " + str(multiplicar(nombres))

        # Mostrem un espai
        print

        # Esperem a que l'usuari prémi una tecla per a continuar
        raw_input('Prém una tecla per a continuar...')

    # Si vol dividir en decimals
    elif (operacio == '4'):
        print 'Dividir (decimals)'

    # Si vol dividir amb residu
    elif (operacio == '5'):
        print 'Dividir (residu)'

    # Si vol fer una arrel quadrada
    elif (operacio == '6'):
        print 'Arrel Quadrada'

    # Si vol sortir
    elif ((operacio == 'S') or (operacio == 's')):
        sortir = True

    # Si no ha introduït una opció correcta
    else:
        print 'Siusplau, introdueix una opció correcta'
        os.system('sleep 5')

# Netejem la pantalla
os.system('clear')
