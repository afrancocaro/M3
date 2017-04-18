# -*- coding: utf-8 -*-

# Imports
from random import randint
import os

# Variables

sortir = False
pals = {1: 'Piques', 2: 'Diamants', 3: 'Trèbols', 4: 'Cors'}
cartes = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'As'}

jwins = 0
mwins = 0
empats = 0

count = 1
totalcount = 1

apostaminima = 10
saldoinicial = 100
saldo = 100

cartesultilitzades = []

while (sortir == False):


	heapostat = False

	while (heapostat == False):

		os.system('clear')

		aposta = input('Quant vols apostar? (saldo = ' + str(saldo) + '): ')

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

	mpal = randint(1, 4)
	mcarta = randint(2, 14)

	sortirjugador = False

	while (sortirjugador == False):

		jpal = randint(1, 4)
		jcarta = randint(2, 14)

		jresultat = (jpal, jcarta)

		if not(jresultat in cartesultilitzades):

			cartesultilitzades.append(jresultat)
			sortirjugador = True

	sortirmaquina = False

	while (sortirmaquina == False):

		mpal = randint(1, 4)
		mcarta = randint(2, 14)

		mresultat = (mpal, mcarta)

		if not(mresultat in cartesultilitzades):

			cartesultilitzades.append(mresultat)
			sortirmaquina = True

	if (jcarta == mcarta):
		print "Empat: Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
		count = count - 1
		empats = empats + 1
		print "El jugador perd " + str(aposta) + "€ i es queda amb un total de " + str(saldo) + "€ perquè hi ha hagut un empat!!"


	elif (jcarta > mcarta):

		print "Ha guanyat el jugador!!: Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
		jwins = jwins + 1
		saldo = saldo + (aposta * 2)
		print "El jugador guanya " + str(aposta) + "€ i es queda amb un total de " + str(saldo) + "€!"

	elif (jcarta < mcarta):

		print "Ha guanyat la màquina :( Jugador = " + cartes[jcarta] + " de " + pals[jpal] + ", Màquina = " + cartes[mcarta] + " de " + pals[mpal]
		mwins = mwins + 1
		print "El jugador perd " + str(aposta) + "€ i es queda amb un total de " + str(saldo) + "€!"

	if ((len(cartesultilitzades) == 52) or (saldo ==  0) or (saldo < apostaminima)):
		sortir = True

	if (sortir == False):

		print
		tecla = raw_input('Vols continuar apostant? (n):')

		if  (tecla == 'n'):
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
