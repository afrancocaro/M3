# coding: utf-8

# Imports
import random

# Definim una llista, una tupla i un diccionari
llista = ['JS', 'HTML', 'CSS']
tupla = ('JS', 'HTML', 'CSS')
diccionari = {'JS': 'JavaScript', 'HTML': 'HyperText Markup Language', 'CSS': 'Cascading StyleSheets'}

print "Llista: " + random.choice(llista)
print "Tupla: " + random.choice(tupla)
print "Diccionari: " + random.choice(diccionari.keys())
