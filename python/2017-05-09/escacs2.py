# coding: utf-8

# myRange
def myRange (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment


# La casella ha de ser blanca o negra?
def blancaNegra(fila, columna):

    # Si la columna i la fila són el mateix tipus de nombre (parell o senar), la casella sempre serà negra. Sinó serà blanca
    if ((fila % 2) == (columna % 2)):

        return "*"

    # Si no és negra, és blanca
    else:

        return " "

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

        fila = fila + str(blancaNegra(f, c))


    # Afegim una línia per fer de límit al taulell
    fila = fila + "|"

    # Mostrem la fila acabada un cop ha passat per a totes les columnes analitzant-les
    print fila

# Delimitem el taulell per fer-lo bonic
print "----------"
