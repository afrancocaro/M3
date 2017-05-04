# coding: utf-8

# myRange
def myRange (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment

# f és fila, c és columna
for f in myRange(1,5,1):

    fila = ""

    for c in myRange(1,4,1):

        if (f == 1):

            if (c == 2):
                fila = fila + "A"

            elif (c == 3):
                fila = fila + "B"

            elif (c == 4):
                fila = fila + "C"
            
            else:
                fila = fila + "-"

        else:

            if (c == 1):
                fila = fila + str(f - 1)

            elif (
                        ((f == 3) and (c == 3))
                    or  ((f == 4) and (c == 2))
                 ):
                fila = fila + "*"

            else:
                fila = fila + "-"

    print fila
