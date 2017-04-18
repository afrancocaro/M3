# -*- coding: utf-8 -*-

#################
#    Imports    #
#################
from random import randint
import os

##################
#    Nivell 3    #
##################

# Apostar
def comprovarAposta():

    if (aposta < apostaminima):

        print "La aposta mínima és de 10"

    elif (aposta > saldo):

        print "No pots apostar més que el teu saldo!!"

    elif (aposta <= saldo):

        if (aposta == saldo):
            print
            print "ALL IN!!"

        saldo = saldo - aposta

        print

        heapostat = True

# Apostar

# Treure Cartes

#### Treure Carta Jugador
def treureCartaJugador():

    sortirjugador = False

    while (sortirjugador == False):

        jpal = randint(1, 4)
        jcarta = randint(2, 14)

        jresultat = (jpal, jcarta)

        if not(jresultat in cartesultilitzades):

            cartesultilitzades.append(jresultat)
            sortirjugador = True


#### Treure Carta Màquina
def treureCartaMaquina():

    sortirmaquina = False

    while (sortirmaquina == False):

        mpal = randint(1, 4)
        mcarta = randint(2, 14)

        mresultat = (mpal, mcarta)

        if not(mresultat in cartesultilitzades):

            cartesultilitzades.append(mresultat)
            sortirmaquina = True


# Treure Cartes

##################
#    Nivell 2    #
##################

# Apostar
def apostar():

    heapostat = False

    while (heapostat == False):

        os.system('clear')

        aposta = input('Quant vols apostar? (saldo = ' + str(saldo) + '): ')

        comprovarAposta()



# Apostar

# Treure Cartes
def treureCartes():

    # Treure Carta Jugador
    treureCartaJugador()

    # Treure Carta Màquina
    treureCartaMaquina()

# Treure Cartes

##################
#    Nivell 1    #
##################

while (sortir == False):

    # Apostar
    apostar()

    # Treure Cartes
    treureCartes()

    # 
