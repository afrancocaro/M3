# coding: utf-8

# 0 PI > LA, TI
# 1 PA > PI, SP
# 2 TI > PA, LA
# 3 LA > PA, SP
#  > PI, TI

from random import randint

player1 = input("Escriu un nombre entre el 0 i el 4 (0 PI, 1 PA, 2 TI, 3 LA, 4 SP): ")
player2 = randint(0,4)

if (player1 == player2):
    print "Empat"

elif ((player1 == 0) and ((player2 == 2) or (player2 == 3))) or ((player1 == 1) and ((player2 == 0) or (player2 == 4))) or ((player1 == 2) and ((player2 == 1) or (player2 == 3))) or ((player1 == 3) and ((player2 == 1) or (player2 == 4))) or ((player1 == 4) and ((player2 == 0) or (player2 == 2))):
    print "Guanya el player1"

else:
    print "Guanya la màquina"
