# -*- coding: utf-8 -*-

# Imports
import random
import os

# Creem una classe per a les cartes
class Carta:

    # Quan creeem una carta (té valor i pal)
    def __init__(self, valor, pal):

        # Cada carte té un valor
        self.valor = valor

        # Si és una J, posa-li com a nom 'J'
        if (valor == 11):
            self.nom = 'J'

        # Si és una J, posa-li com a nom 'J'
        elif (valor == 12):
            self.nom = 'Q'

        # Si és una J, posa-li com a nom 'J'
        elif (valor == 13):
            self.nom = 'K'

        # Si és una J, posa-li com a nom 'J'
        elif (valor == 14):
            self.nom = 'As'

        # Si no és una figura o un As, posa-li el nom que li correspongui
        else:
            self.nom = str(valor)

        # Cada carta té un pal
        self.pal = pal

    # Mostrar la carta de forma bonica
    def mostrar(self):

        # Retornem un string del valor de la carta i del seu pal
        return self.nom + ' de ' + self.pal

def barrejarCartes():

    # Creem una llista amb totes les cartes (buida)
    cartes = []

    # Hi afegim totes les cartes
    cartes.append(Carta(2, 'Diamants'))
    cartes.append(Carta(3, 'Diamants'))
    cartes.append(Carta(4, 'Diamants'))
    cartes.append(Carta(5, 'Diamants'))
    cartes.append(Carta(6, 'Diamants'))
    cartes.append(Carta(7, 'Diamants'))
    cartes.append(Carta(8, 'Diamants'))
    cartes.append(Carta(9, 'Diamants'))
    cartes.append(Carta(10, 'Diamants'))
    cartes.append(Carta(11, 'Diamants')) # J
    cartes.append(Carta(12, 'Diamants')) # Q
    cartes.append(Carta(13, 'Diamants')) # K
    cartes.append(Carta(14, 'Diamants')) # As

    cartes.append(Carta(2, 'Cors'))
    cartes.append(Carta(3, 'Cors'))
    cartes.append(Carta(4, 'Cors'))
    cartes.append(Carta(5, 'Cors'))
    cartes.append(Carta(6, 'Cors'))
    cartes.append(Carta(7, 'Cors'))
    cartes.append(Carta(8, 'Cors'))
    cartes.append(Carta(9, 'Cors'))
    cartes.append(Carta(10, 'Cors'))
    cartes.append(Carta(11, 'Cors')) # J
    cartes.append(Carta(12, 'Cors')) # Q
    cartes.append(Carta(13, 'Cors')) # K
    cartes.append(Carta(14, 'Cors')) # As

    cartes.append(Carta(2, 'Trèvols'))
    cartes.append(Carta(3, 'Trèvols'))
    cartes.append(Carta(4, 'Trèvols'))
    cartes.append(Carta(5, 'Trèvols'))
    cartes.append(Carta(6, 'Trèvols'))
    cartes.append(Carta(7, 'Trèvols'))
    cartes.append(Carta(8, 'Trèvols'))
    cartes.append(Carta(9, 'Trèvols'))
    cartes.append(Carta(10, 'Trèvols'))
    cartes.append(Carta(11, 'Trèvols')) # J
    cartes.append(Carta(12, 'Trèvols')) # Q
    cartes.append(Carta(13, 'Trèvols')) # K
    cartes.append(Carta(14, 'Trèvols')) # As

    cartes.append(Carta(2, 'Piques'))
    cartes.append(Carta(3, 'Piques'))
    cartes.append(Carta(4, 'Piques'))
    cartes.append(Carta(5, 'Piques'))
    cartes.append(Carta(6, 'Piques'))
    cartes.append(Carta(7, 'Piques'))
    cartes.append(Carta(8, 'Piques'))
    cartes.append(Carta(9, 'Piques'))
    cartes.append(Carta(10, 'Piques'))
    cartes.append(Carta(11, 'Piques')) # J
    cartes.append(Carta(12, 'Piques')) # Q
    cartes.append(Carta(13, 'Piques')) # K
    cartes.append(Carta(14, 'Piques')) # As

    # Retornem la variable cartes
    return cartes

def treureCarta(baralla):

    # Treiem una carta
    carta = random.choice(baralla)

    # L'esborrem de la baralla (ja s'ha treta)
    baralla.remove(carta)

    # Retornem la carta + llista de les cartes actualitzades
    return carta, baralla

def comprovarGuanyador(cartaJugador, cartaMaquina, estadistiques):

    # Si guanya el jugador
    if (cartaJugador.valor > cartaMaquina.valor):

        # Sumem 1 al comptador del jugador (a la positicó 1 hi han les estadístiques del jugador)
        estadistiques[1] = estadistiques[1] + 1

        # Retornem que guanya el jugador + les estadístiques actualitzades
        return 1, estadistiques

    # Si guanya la màquina
    elif (cartaJugador.valor < cartaMaquina.valor):

        # Sumem 1 al comptador de la màquina (a la positicó 2 hi han les estadístiques del màquina)
        estadistiques[2] = estadistiques[2] + 1

        # Retornem que guanya la màquina + les estadístiques actualitzades
        return 2, estadistiques

    # Hi ha un empat
    else:

        # Sumem 1 al comptador d'empats (és a la postició 3 de les estadístiques)
        estadistiques[3] = estadistiques[3] + 1

        # Restem 1 al comptador de partides útils (és a la posició 0 de les estadístiques)
        estadistiques[0] = estadistiques[0] - 1

        # Retornem que hi ha hagut un empat + les estadístiques actualitzades
        return 0, estadistiques

def mostrarResultat(resultat, cartaJugador, cartaMaquina):

    # Si guanya el Jugador
    if (resultat == 1):

        # Mostrem un missatge + les cartes que s'han tret
        print "Ha guanyat el jugador! (Jugador: " + cartaJugador.mostrar() + ", Màquina: " + cartaMaquina.mostrar() + ")"

    # Si guanya la màquina
    elif (resultat == 2):

        # Mostrem un missatge + les cartes que s'han tret
        print "Ha guanyat la màquina! (Jugador: " + cartaJugador.mostrar() + ", Màquina: " + cartaMaquina.mostrar() + ")"

    # Si hi ha hagut un empat
    else:
        # Mostrem un missatge + les cartes que s'han tret
        print "Hi ha hagut un empat! (Jugador: " + cartaJugador.mostrar() + ", Màquina: " + cartaMaquina.mostrar() + ")"

def mostrarEstadistiques(estadistiques, totalPartides):

    print
    print "------ ESTADÍSTIQUES -------"
    print
    print "S'han jugat " + str(totalPartides) + " partides"
    print "Hi han hagut " + str(estadistiques[3]) + " empats"
    print "El Jugador ha guanyat un " + str(round(((float(estadistiques[1]) * 100) / float(estadistiques[0])), 2)) + "% de les partides (" + str(estadistiques[1]) + ")"
    print "La màquina ha guanyat un " + str(round(((float(estadistiques[2]) * 100) / float(estadistiques[0])), 2)) + "% de les partides (" + str(estadistiques[2]) + ")"

# Esborrem la pantalla
os.system('clear')

# Inicialitzem les variables per al loop
sortir = False
estadistiques = [0, 0, 0, 0]
count = 0

# Creem la baralla de cartes
cartes = barrejarCartes()

# Loop principal
while (sortir == False):

    # Treiem una carta per al jugador i actualitzem la baralla
    cartaJugador, cartes = treureCarta(cartes)

    # Treiem una carta per a la màquina i actualitzem la baralla
    cartaMaquina, cartes = treureCarta(cartes)

    # Comprovem qui guanya i actualitzem les estadístiques
    resultat, estadistiques = comprovarGuanyador(cartaJugador, cartaMaquina, estadistiques)

    # Mostrem el resultat a l'usuari
    mostrarResultat(resultat, cartaJugador, cartaMaquina)

    # Comprovem si hem de continuar dins del loop
    if (len(cartes) == 0):

        # Sortim del bucle
        sortir = True

    # Augmentem els comptadors de partides
    count = count + 1
    estadistiques[0] = estadistiques[0] + 1

# Mostrem les estadístiques
mostrarEstadistiques(estadistiques, count)
