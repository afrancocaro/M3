# coding: utf-8

# Imports
import os
import stat

def permisos(path):

    # Definim les llistes dels permisos
    permisosDirectoris = []
    permisosFitxers = []

    # Per cada directori i subdirectori a la ruta especificada
    for currentPath, dirs, files in os.walk(path):

        # Per cada subdirectori a dins del directori actual
        for dir in dirs:

            # Fem una ruta absoluta d'aquest
            rutaDir = os.path.join(currentPath, dir)

            # Mirem els permisos d'aquest
            permisosDir = oct(stat.S_IMODE ( os.stat (rutaDir).st_mode ))

            # Si els permisos no existeixen a la llista, els afegim
            if not(permisosDir in permisosDirectoris):

                # Afegim els permisos dels fitxer
                permisosDirectoris.append(permisosDir)


        # Per cada fitxer al directori actual (del loop)
        for file in files:

            # Fem una ruta absoluta d'aquest
            rutaFile = os.path.join(currentPath, file)

            # Mirem els permisos d'aquest
            permisosFile = oct(stat.S_IMODE ( os.stat (rutaFile).st_mode ))

            # Si els permisos no existeixen a la llista, els afegim
            if not(permisosFile in permisosFitxers):

                # Afegim els permisos dels fitxer
                permisosFitxers.append(permisosFile)


    # Mostrem els permisos que hi ha als directoris dins del directori principal i els seus subdirectoris
    print "Permisos dels Directoris"
    print permisosDirectoris

    print # Enter

    # Mostrem els permisos que hi ha als fitxers dins del directori prinicipal i els seus subdirectoris
    print "Permisos dels Fitxers"
    print permisosFitxers

# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

permisos(path)
