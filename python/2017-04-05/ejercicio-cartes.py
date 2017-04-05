# -*- coding: utf-8 -*-

# Imports
from random import randint

# Variables

sortir = False
pals = {1: 'Piques', 2: 'Diamants', 3: 'Trèbols', 4: 'Cors'}
cartes = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'As'}

jwins = 0
mwins = 0
empats = 0

count = 1
totalcount = 1

while (sortir == False):
	
	jpal = randint(1, 4)
	jcarta = randint(2, 14)
	mpal = randint(1, 4)
	mcarta = randint(2, 14)
	
	if (jcarta == mcarta):
		
		print "Empat: Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
		empats = empats + 1
		count = count - 1
		
		
	elif (jcarta > mcarta):
		
		print "Ha guanyat el jugador!!: Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
		jwins = jwins + 1
		
	elif (jcarta < mcarta):
		
		print "Ha guanyat la màquina :( Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
		mwins = mwins + 1		
	
	tecla = raw_input('Vols sortir? (y, n): ')
	
	if (tecla == 'y'):
		sortir = True
		
	count = count + 1
	totalcount = totalcount + 1
	
# La última volta altera els resultats
count = count - 1
totalcount = totalcount - 1

print
print "------ ESTADÍSTIQUES -------"
print 
print "S'han jugat " + str(totalcount) + " partides"
print "Hi han hagut " + str(empats) + " empats"
print "El Jugador ha guanyat un " + str((jwins * 100) / count) + "% de les partides (" + str(jwins) + ")"
print "La màquina ha guanyat un " + str((mwins * 100) / count) + "% de les partides (" + str(mwins) + ")"
