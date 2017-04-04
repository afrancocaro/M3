# coding: utf-8

num = 31
sortir = False

while (sortir == False):

    player1 = num % 7
    player2 = num % 5

    # Player 1
    if (player1 == 0) or (player1 == 1):
        player1 = "tisores"
    elif (player1 == 2) or (player1 == 3) or (player1 == 6):
        player1 = "pedra"
    elif (player1 == 4) or (player1 == 5):
        player1 = "paper"

    # Player 2
    if (player2 == 0) or (player2 == 1) or (player2 == 2):
        player2 = "paper"
    elif (player2 == 3):
        player2 = "tisores"
    elif (player2 == 4):
        player2 = "pedra"

    # Who wins
    if (player1 == player2):
        print "Empat"
    elif ((player1 == "pedra" and player2 == "tisores") or (player1 == "paper" and player2 == "pedra") or (player1 == "tisores" and player2 == "paper")):
        print "Player 1 wins"
    else:
        print "Player 2 wins"

    if (num == 57):
        sortir = True

    num = num + 1
