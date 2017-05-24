# coding: utf-8

# Imports
import os
import stat

# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

# Per cada directori i subdirectori a la ruta especificada
for currentPath, dirs, files in os.walk(path):

    
