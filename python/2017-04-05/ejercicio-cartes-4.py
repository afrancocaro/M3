# -*- coding: utf-8 -*-

#################
#    Imports    #
#################
from random import randint
import os

###########################
#    Variables Globals    #
###########################

sortir = False
pals = {1: 'Piques', 2: 'Diamants', 3: 'Trèbols', 4: 'Cors'}
cartes = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'As'}
cartesultilitzades = []

jwins = 0
mwins = 0
empats = 0

count = 1
totalcount = 1

aposta = 0
apostaminima = 10
saldoinicial = 100
saldo = 100


##################
#    Nivell 3    #
##################

# Apostar
def comprovarAposta():

    # Global Vars
    global saldo

    # Function
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

    # Global Vars
    global jpal
    global jcarta
    global jresultat
    global cartesultilitzades

    # Function
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

    # Global Vars
    global mpal
    global mcarta
    global mresultat
    global cartesultilitzades

    # Function
    sortirmaquina = False

    while (sortirmaquina == False):

        mpal = randint(1, 4)
        mcarta = randint(2, 14)

        mresultat = (mpal, mcarta)

        if not(mresultat in cartesultilitzades):

            cartesultilitzades.append(mresultat)
            sortirmaquina = True


# Treure Cartes

# Qui guanya

#### Hi ha un empat
def guanyaEmpat():

    # Global Vars
    global count
    global empats

    # Function
    print "Empat: Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
    count = count - 1
    empats = empats + 1
    print "El jugador perd " + str(aposta) + "€ i es queda amb un total de " + str(saldo) + "€ perquè hi ha hagut un empat!!"


#### Guanya el jugador
def guanyaJugador():

    # Global Vars
    global jwins
    global saldo

    # Function
    print "Ha guanyat el jugador!!: Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
    jwins = jwins + 1
    saldo = saldo + (aposta * 2)
    print "El jugador guanya " + str(aposta) + "€ i es queda amb un total de " + str(saldo) + "€!"


#### Guanya la màquina
def guanyaMaquina():

    # Global Vars
    global mwins

    # Function
    print "Ha guanyat la màquina :( Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
    mwins = mwins + 1
    print "El jugador perd " + str(aposta) + "€ i es queda amb un total de " + str(saldo) + "€!"


# Qui guanya

##################
#    Nivell 2    #
##################

# Apostar
def apostar():

    # Global Vars
    global aposta

    # Function
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

# Qui guanya

def quiGuanya():

    # Empat
    if (jcarta == mcarta):

        guanyaEmpat()

    # Jugador
    elif (jcarta > mcarta):

        guanyaJugador()

    # Màquina
    elif (jcarta < mcarta):

        guanyaMaquina()



# Qui guanya

# Sortir

def sortir():

    if ((len(cartesultilitzades) == 52) or (saldo ==  0) or (saldo < apostaminima)):
		sortir = True

    if (sortir == False):

        print
        tecla = raw_input('Vols continuar apostant? (n):')

        if  (tecla == 'n'):
            sortir = True


# Sortir

def augmentVariables():

    count = count + 1
    totalcount = totalcount + 1

# Augment Variables

# Estadístiques

def estadistiques():

    # La última volta altera els resultats
    count = count - 1
    totalcount = totalcount - 1

    print
    print "------ ESTADÍSTIQUES -------"
    print
    print "S'han jugat " + str(totalcount) + " partides"
    print "Hi han hagut " + str(empats) + " empats"
    print
    print "El Jugador ha guanyat un " + str((jwins * 100) / count) + "% de les partides (" + str(jwins) + ")"
    print "La màquina ha guanyat un " + str((mwins * 100) / count) + "% de les partides (" + str(mwins) + ")"
    print

    if (saldoinicial == saldo):
    	print "El jugador s'ha quedat amb el mateix saldo que ha començat (" + str(saldo) + ")"

    elif (saldoinicial > saldo):
    	print "El jugador ha perdut " + str(saldoinicial - saldo) + "€"

    elif (saldoinicial < saldo):
    	print "El jugador ha guanyat " + str(saldo - saldoinicial) + "€!!!"

    print "El jugador s'ha quedat amb " + str(saldo) + "€"

# Estadístiques

##################
#    Nivell 1    #
##################
sortir = False



while (sortir == False):

    # Apostar
    apostar()

    # Treure Cartes
    treureCartes()

    # Qui Guanya?
    quiGuanya()

    # Sortir
    sortir()

    # Augment Variables
    augmentVariables()


# Estadístiques After Loop
estadistiques()
