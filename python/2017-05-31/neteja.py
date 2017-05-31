# coding: utf-8

# Imports
import os
import time

def llistaNeteja(path):

    # Per cada fitxer i directori (de forma recursiva) què hi hagi al path
    for currentPath, dirs, files in os.walk(path):

        # Per cada fitxer que s'analitzi
        for file in files:

            # Ruta absoluta d'aquest
            filePath = os.path.join(currentPath, file)

            # Data de fa un any
            yearAgo = time.ctime()[:-4] + str(int(time.ctime()[-4:]) - 1)

            # Si el fitxer pesa més d'una giga i fa més d'un any que no s'ha accedit
            if ((os.stat(filePath).st_size >= 1024 ** 3) and ((time.ctime(os.path.getatime(filePath))) > yearAgo)):

                print filePath


# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

# Netjem la pantalla
os.system('clear')

# Cridem a la acció
llistaNeteja(path)
