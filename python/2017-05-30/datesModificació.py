# coding: utf-8

# Imports
import os
import time

def datesModificacio(path):

    # Per cada directori i subdirectori d'aquest
    for currentPath, dirs, files in os.walk(path):

        # Per cada fitxer a dins del directori o subdirectori actual
        for file in files:

            # Ruta del fitxer actual
            filePath = os.path.join(currentPath, file)

            # Mostrem la info relacionada amb les dates
            print filePath + ":"
            print "Data d'última modificació: " + str(time.ctime(os.path.getmtime(filePath)))
            print "Data d'últim accés: " + str(time.ctime(os.path.getatime(filePath)))
            print # Enter



# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

# Netjem la pantalla
os.system('clear')

# Cridem a la acció
datesModificacio(path)
