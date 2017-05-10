# coding: utf-8

# myRange
def myRange (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment

# El nombre és parell o senar?
def tipusNombre(nombre):

    # Si el residu del nombre entre 2 és 0, el nombre és parell. Sinó, serà senar
    if (nombre % 2 == 0):

        # Retornem true (true és per als nombres parells)
        return True

    # Si no és parell, és senar
    else:

        # Retornem false (false és per als nombres parells)
        return False


# f --> fila, c --> columna
# * --Z negra, " " --> blanca

# Delimitem el taulell per fer-lo bonic
print "__________"

# Per cada fila (8)
for f in myRange(1, 8, 1):

    # Resetejem la variable fila que serveix per mostrar tot el text en una línia
    fila = "|" # Afegim una línia per fer de límit al taulell

    # Per cada columna (8)
    for c in myRange(1, 8, 1):

        # Si la columna i la fila són el mateix tipus de nombre (parell o senar), la casella sempre serà negra. Sinó serà blanca
        if (tipusNombre(f) == tipusNombre(c)):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "*"

        # Si no és una casella negra, serà una casella blanca
        else:

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + " "

    # Afegim una línia per fer de límit al taulell
    fila = fila + "|"

    # Mostrem la fila acabada un cop ha passat per a totes les columnes analitzant-les
    print fila

# Delimitem el taulell per fer-lo bonic
print "----------"
