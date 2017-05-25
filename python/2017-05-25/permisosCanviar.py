# coding: utf-8

# Imports
import os
import stat

# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a modificar: ')

# Per cada directori i subdirectori a la ruta especificada
for currentPath, dirs, files in os.walk(path):

        # Per cada directori al directori actual (del loop)
        for dir in dirs:

            # Fem una ruta absoluta d'aquest
            rutaDir = os.path.join(currentPath, dir)

            # Canviem els permisos a 0777
            os.chmod(rutaDir, 0777)


        # Per cada fitxer al directori actual (del loop)
        for file in files:

            # Fem una ruta absoluta d'aquest
            rutaFile = os.path.join(currentPath, file)

            # Canviem els permisos a 0700
            os.chmod(rutaFile, 0700)
