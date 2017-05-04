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

            elif (c == 5):
                fila = fila + "D"

            else:
                fila = fila + "-"

        elif (f == 2):

            if (c == 1):
                fila = fila + "1"

            else:
                fila = fila + "-"


        elif (f == 3):

            if (c == 1):
                fila = fila + "2"

            elif (c == 3):
                fila = fila + "*"

            else:
                fila = fila + "-"

        elif (f == 4):

            if (c == 1):
                fila = fila + "3"

            elif (c == 2):
                fila = fila + "*"

            else:
                fila = fila + "-"

        elif (f == 5):

            if (c == 1):
                fila = fila + "4"

            else:
                fila = fila + "-"

    print fila    
