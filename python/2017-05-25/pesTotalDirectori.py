# coding: utf-8

# Imports
import os

def pesTotal(path):

    # Inicialitzem el pes total a 0
    pes = 0

    # Per cada directori i subdirectori a la ruta especificada
    for currentPath, dirs, files in os.walk(path):

        # Per cada directori al directori actual (del loop)
        for dir in dirs:

            print dir

            # Fem una ruta absoluta d'aquest
            # rutaDir = os.path.join(currentPath, dir)
            #
            # # Sumem el pes d'aques directori al pes total
            # pes = pes + rutaDir.os.stat(rutaDir).st_size

        # Per cada fitxer al directori actual (del loop)
        for file in files:

            print file

            # Fem una ruta absoluta d'aquest
            # rutaFile = os.path.join(currentPath, file)
            #
            # # Sumem el pes d'aques directori al pes total
            # pes = pes + rutaDir.os.stat(rutaFile).st_size


    # Retornem el pes total de tota la carpeta i dels subdirectoris d'aquesta
    return pes


# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

print path + ": " + str(pesTotal(path))
