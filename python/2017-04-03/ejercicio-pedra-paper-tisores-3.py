# coding: utf-8

# Imports
from random import randint
import os

# Clear
os.system('clear')

# Vars
num = 1
sortir = False
player1wins = 0
player2wins = 0
empats = 0

# Loop
while (sortir == False):

    # Player 1
    player1 = randint(0,2)

    # Player 2
    player2 = randint(0,2)

    # Who wins
    if (player1 == player2):
        print "Empat"
        empats = empats + 1

    elif ((player1 == 0 and player2 == 2) or (player1 == 1 and player2 == 0) or (player1 == 2 and player2 == 1)):
        print "Player 1 wins"
        player1wins = player1wins + 1
    else:
        print "Player 2 wins"
        player2wins = player2wins + 1

    if (num == 10):
        sortir = True

    num = num + 1

print "-----------------"
print "- ESTADÍSTIQUES -"
print "-----------------"
print "El jugador 1 ha guanyat un " + str(player1wins * 10) + "% de les partides"
print "El jugador 2 ha guanyat un " + str(player2wins * 10) + "% de les partides"
print "Hi ha hagut un " + str(empats * 10) + "% d'empats"
