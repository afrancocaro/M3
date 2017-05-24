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

            # Fem una ruta absoluta d'aquest
            rutaDir = os.path.join(currentPath, dir)

            # Sumem el pes d'aques directori al pes total
            pes = pes + os.stat(rutaDir).st_size

        # Per cada fitxer al directori actual (del loop)
        for file in files:

            # Fem una ruta absoluta d'aquest
            rutaFile = os.path.join(currentPath, file)

            # Sumem el pes d'aques directori al pes total
            pes = pes + os.stat(rutaFile).st_size


    # Retornem el pes total de tota la carpeta i dels subdirectoris d'aquesta
    return pes

def canviUnitat(pes):

    # Definim la variable de contador
    count = 0

    # Mentres que el pes no sigui menor que 1024, continuem dividint
    while (pes >= 1024):

        # Dividim pes entre 1024 (canviem la unitat)
        pes = pes / 1024

        # Augmentem en 1 el contador
        count = count + 1

    # Si no s'ha canviat la unitat, està en Bytes
    if (count == 0):

        return str(pes) + 'B'

    # Si ho hem transformat a KiloBytes
    elif (count == 1):

        return str(pes) + 'KB'

    # Si ho hem transformat a MegaBytes
    elif (count == 2):

        return str(pes) + 'MB'

    # Si ho hem transformat a GigaBytes
    elif (count == 3):

        return str(pes) + 'GB'

# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

pes = pesTotal(path)

# Passem el pes a KB, MB o GB
print path + ': ' + canviUnitat(pes)
