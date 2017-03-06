# coding: utf-8

# Importem les funcions de l'ordinador
import os

# Netejem la pantalla
os.system('clear')

# Espera a que l'usuari introdueixi la edat
edat = input('Siusplau, introdueix la teva edat: ')

# Netejem la pantalla
os.system('clear')

# Si està entre 18 i 23 anys
if (edat >=  18) and (edat <= 23):

	# Mostrem per pantalla que l'usuari pot entrar
	print "Pots entrar, ets un jove"

# Si l'edat és menor que 18
elif edat < 18:

	# Mostrem per pantalla que l'usuari no pot entrar perquè és massa petit
	print "Ets massa petit per entrar"

# Si l'edat és major que 23
else:

	# Mostrem per pantalla que l'usuari no pot entrar perquè és massa petit
	print "Ets massa gran per entrar"
