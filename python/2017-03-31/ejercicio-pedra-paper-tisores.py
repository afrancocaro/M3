# coding: utf-8

player1 = raw_input("Player 1:")
player2 = raw_input("player2:")

if (player1 == player2):
    print "Empat"
elif ((player1 == "pedra" and player2 == "tisores") or (player1 == "paper" and player2 == "pedra") or (player1 == "tisores" and player2 == "paper")):
    print "Player 1 wins"
else:
    print "Player 2 wins"
