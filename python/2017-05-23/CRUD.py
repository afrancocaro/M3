# coding: utf-8

# Imports
import os

def create(dict):

    # Netejem la pantalla
    os.system('clear')

    # Demanem a l'usuari la clau
    clau = raw_input('Quina clau vols posar-hi? ')
    contingut = raw_input('Quin valor vols que tingui la clau "' + clau + '"? ')

    # Afegim la clau al diccionari
    dict[clau] = contingut

    # Retornem el diccionari
    return dict

def read(dict):

    # Netejem la pantalla
    os.system('clear')

    # Per cada item al diccionari, mostra'l de forma bonica
    for item in dict:

        # Mostrem l'item
        print item + ': ' + dict[item]

    print # Enter
    print # Enter
    # Esperem a que l'usuari vulgui continuar
    raw_input('Prem qualsevol tecla per a continuar...')


def update(dict):

    # Netejem la pantalla
    os.system('clear')

    # Per cada item al diccionari, mostra'l de forma bonica
    for item in dict:

        # Mostrem l'item
        print '"' + item + '"' + ' (' + dict[item] + ')'

    print # Enter
    print # Enter

    # Esperem a que l'usuari trii
    clau = raw_input('Quina clau vols modificar? ')

    # Esperem a que l'usuari posi el valor
    contingut = raw_input('Quin contingut vols que tingui? ')

    # Actualitzem el contingut
    dict[clau] = contingut

    # Retornem el diccionari
    return dict

def delete(dict):

    # Netejem la pantalla
    os.system('clear')

    # Per cada item al diccionari, mostra'l de forma bonica
    for item in dict:

        # Mostrem l'item
        print '"' + item + '"' + ' (' + dict[item] + ')'

    print # Enter
    print # Enter

    # Esperem a que l'usuari trii
    clau = raw_input('Quina clau vols esborrar? ')

    # Esborrem la clau
    del dict[clau]

    # Retornem el diccionari
    return dict


# Variables per al loop
sortir = False
dict = {}

# Menú
while (sortir == False):

    # Netejem la pantalla
    os.system('clear')

    # Mostrem el menú
    print "1- Create"
    print "2- Read"
    print "3- Update"
    print "4- Delete"
    print # Enter
    print "0- Sortir"
    print # Enter

    # L'usuari tria quina opció
    opcio = input('Quina opció vols triar? ')

    # Si volem afegir contingut
    if (opcio == 1):

        # Cridem a la funció per crear contingut
        dict = create(dict)

    # Si volem llegir
    elif (opcio == 2):

        # Cridem a la acció per llegir el contingut
        read(dict)

    # Si volem modificar
    elif (opcio == 3):

        # Cridem la acció per actualitzar el contingut
        dict = update(dict)

    # Si volem esborrar
    elif (opcio == 4):

        # Cridem la opcio per a esborrar
        dict = delete(dict)

    # Si volem sortir del programa
    elif (opcio == 0):

        # Sortir
        sortir = True

# Netejem la pantalla
os.system('clear')
