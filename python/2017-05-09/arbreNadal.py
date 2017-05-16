# coding: utf-8

# myRange
def myRange (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment


# f --> fila, c --> columna
# Per cada fila (6)
for f in myRange(1, 6, 1):

    # Resetejem la variable fila que serveix per mostrar tot el text en una línia
    fila = ""

    # Per cada columna (5)
    for c in myRange(1, 5, 1):

        # Si la casella és la casella de l'estrella (1, 3)
        if ((f == 1) and (c == 3)):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "*"

        # Si la casella és una casella de fulles (4 | 3,[2-4] | 2,3)
        elif (
            (f == 4) or
            ((f == 3) and (
                (c == 2) or
                (c == 3) or
                (c == 4))
            ) or
            ((f == 2) and (c == 3))
        ):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "A"

        # Si la casella és una casella de tronc ([4-5],3)
        elif (

            (
                (f == 5) or
                (f == 6)
            ) and (c == 3)
        ):

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + "N"

        # Si no s'ha complert cap condició anterior, és un espai en blanc
        else:

            # Afegim el valor a la variable que ho mostrarà
            fila = fila + " "

    # Mostrem la fila acabada un cop ha passat per a totes les columnes analitzant-les
    print fila
