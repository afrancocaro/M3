# coding: utf-8

# Importem les funcions del sistema
import os

# Netejem la pantalla
os.system('clear')

# Esperem a que l'usuari introdueixi un nombre
nombre = input('Siusplau, introdueix un nombre per comprovar si és un nombre parell o no: ')

# Fem un espai
print

# Si el residu és 0 (és parell)
if nombre % 2 == 0:
	print "El nombre " + str(nombre) + " és un nombre parell"

# Si no és parell
else:
	print "El nombre " + str(nombre) + " és un nombre senar"
