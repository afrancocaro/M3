# coding: utf-8

# Imports
import os
import stat

def permisos(path):

    # Per cada directori i subdirectori a la ruta especificada
    for currentPath, dirs, files in os.walk(path):

        print os.stat(currentPath).st_mode
        print stat(currentPath).S_IRWXU

# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

permisos(path)
