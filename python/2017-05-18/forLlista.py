# coding: utf-8

# Definim la llista
llista = ['a', 'b', 'h', 'r', 'z', 'r', 'd', 'y']

# Mostrem la llista
print llista

# Per cada item a la llista, si és una 'r' l'esborrem
for i in llista:

    # Si l'item és una 'r', l'esborrem
    if (i == 'r'):

        # Esborrem de la llista la 'r'
        llista.remove('r')

# Mostrem la llista
print llista
