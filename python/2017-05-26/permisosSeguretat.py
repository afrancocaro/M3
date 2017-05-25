# coding: utf-8

# Imports
import os
import stat

def permisosSeguretat(path):

    # Definim les llistes dels permisos
    directorisInsegurs = []
    fitxersInsegurs = []

    # Per cada directori i subdirectori a la ruta especificada
    for currentPath, dirs, files in os.walk(path):

        # Per cada subdirectori a dins del directori actual
        for dir in dirs:

            # Fem una ruta absoluta d'aquest
            rutaDir = os.path.join(currentPath, dir)

            # Mirem els permisos d'aquest
            permisosDir = oct(stat.S_IMODE ( os.stat (rutaDir).st_mode ))

            # Si els permisos per als altres no són 0 (cap), afegeix el directori a la llista de directoris insegurs
            if (permisosDir[-1] != 0):

                # Afegim el directori a la llista de directoris insegurs
                directorisInsegurs.append(rutaDir)


        # Per cada fitxer al directori actual (del loop)
        for file in files:

            # Fem una ruta absoluta d'aquest
            rutaFile = os.path.join(currentPath, file)

            # Mirem els permisos d'aquest
            permisosFile = oct(stat.S_IMODE ( os.stat (rutaFile).st_mode ))

            # Si els permisos per als altres no són 0 (cap), afegeix el directori a la llista de fitxers insegurs
            if (permisosFile[-1] != 0):

                # Afegim el directori a la llista de fitxers insegurs
                fitxersInsegurs.append(rutaFile)

    # Missatge per dir que ara mostrarem directoris
    print "Directoris:"
    print # Enter

    # Per cada directori insegur, mostra'l
    for item in directorisInsegurs:

        # El mostrem
        print item


    print # Enter
    print # Enter

    # Missatge per dir que ara mostrarem fitxers
    print "Fitxers:"
    print # Enter

    # Per cada directori insegur, mostra'l
    for item in fitxersInsegurs:

        # El mostrem
        print item

# Demanem a l'usuari que ens introdueixi la ruta
path = raw_input('Siusplau, introdueix la ruta absoluta del directori a analitzar: ')

# Netjem la pantalla
os.system('clear')

permisosSeguretat(path)
