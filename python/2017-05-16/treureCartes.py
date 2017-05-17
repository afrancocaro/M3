# coding: utf-8

# Imports
import random

# Llista de totes les cartes
cartes = ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', '1T', '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '10T', 'JT', 'QT', 'KT', '1P', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']

# Mentres quedin cartes
while (len(cartes) != 0):

    # Treiem una carta aleatòria (item de la llista)
    carta = random.choice(cartes)

    # Mostrem la carta treta
    print carta

    # L'esborrem de la llista amb les cartes que queden
    cartes.remove(carta)

    # Mostrem quantes cartes queden
    print 'Queden ' + str(len(cartes)) + ' cartes'
