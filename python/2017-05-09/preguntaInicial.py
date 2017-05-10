# coding: utf-8

# ********
# *  ..  *
# *  \/  *
# ********

# myRange
def myRange (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment

# f --> fila, c --> columna
# Per cada fila (4)
for f in myRange(1, 4, 1):

    # Resetejem la variable fila que serveix per mostrar tot el text en una línia
    fila = ""

    # Per cada columna (8)
    for c in myRange(1, 8, 1):

        # Si és una fila a l'extrem de la figura (que és tota de *)
        if ((f == 1) or (f == 4)):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "*"


        # Si no, si és una columna a l'extrem de la figura (que és tota de *)
        elif ((c == 1) or (c == 8)):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "*"

        # Si no, si és un dels dos quadrants els quals tenen un ull (2,4 i 2,5)
        elif ((f == 2) and ((c == 4) or (c == 5))):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "."

        # Si no, si és el quadrant que té la contrabarra que és la part dreta de la mandíbula (3,4)
        elif ((f == 3) and (c == 4)):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "\\" # Escapem el caràcter \

        # Si no, si és el quadrant que té la barra que és la part esquerra de la mandíbula (3,5)
        elif ((f == 3) and (c == 5)):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "/"

        # Si no s'ha complert cap condició anterior, és un espai en blanc
        else:

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + " "

    # Mostrem la fila acabada un cop ha passat per a totes les columnes analitzant-les
    print fila
