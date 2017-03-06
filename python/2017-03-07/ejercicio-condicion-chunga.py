# coding: utf-8

# Importar les funcions del sistema
import os

# Netejem la pantalla
os.system('clear')

# Esperem a que l'usuari introdueixi un nombre
nombre = input('Siusplau, introdueix un nombre: ')

# Mostrem un espai
print 

# Si el nombre és parell
if (nombre % 2 == 0) and ((nombre >= -10) and (nombre <= 40)) and (nombre < 0):

	# Mostrem per pantalla un missatge que diu que el nombre compleix les condicions
	print "El nombre " + str(nombre) + " compleix les condicions"

# Si el nombre no compleix les condicions
else:

	# Mostrem per pantalla un missatge que diu que el nombre no compleix les condicions
	print "El nombre " + str(nombre) + " NO compleix les condicions"
