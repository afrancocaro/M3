# coding: utf-8

# Imports
import calendar
import os

# myRange
def myRange (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment

# Mostrar mes
def mostrarMes(mes, any):

    # Comptador de dies
    count = 1

    # Mostrem els dies de la setmana
    print "| Dl | Dm | Dc | Dj | Dv | Ds | Du | "
    print "|----|----|----|----|----|----|----| "

    # Files (hi poden haver fins a 6 setmanes)
    for f in myRange(1, 6, 1):

        # Resetejem la variable fila a ""
        fila = "| "

        # Columnes (hi ha 7 dies de la setmana)
        for c in myRange(1, 7, 1):

            # Si estem a la primera setmana (hem de tractar els espais en blanc)
            if (f == 1):

                # Si estem a una columna que ja ha de mostrar dies ()
                if (c >= (calendar.weekday(any, mes, 1) + 1)): # Els dies van de 0 a 6 (0 és Dilluns)

                    # Afegim el dia a la fila que hem d'imprimir
                    fila = fila + str(count).zfill(2) + " | " # Zfill és una funció perquè tots els nombres siguin de dues xifres p. ex. (01)

                    # Augmentem el dia
                    count = count + 1

                # Si encara no hem de mostrar nombres (no estem a la columna correcta)
                else:

                    # Afegim un espai a la fila que hem d'imprimir
                    fila = fila + "   | "

            # Si encara hem d'imprimir nombres (no hem superat el màxim de dies del mes)
            elif (count <= (calendar.monthrange(any, mes)[1])): # La funció retorna una llista de dos items: el primer dia i l'últim. Agafem l'últim

                    # Afegim el dia a la fila que hem d'imprimir
                    fila = fila + str(count).zfill(2) + " | " # Zfill és una funció perquè tots els nombres siguin de dues xifres p. ex. (01)

                    # Augmentem el dia
                    count = count + 1
            # Si hem de parar de mostrar nombres
            else:

                # Afegim un espai a la fila que hem d'imprimir
                fila = fila + "   | "


        # Mostrem la fila completa
        print fila


# Demanem quin mes de quin any volem mostrar
mes = input('Quin mes vols veure (1-12)? ')
any = input('Quin any vols veure (YYYY)? ')

# Netejem la pantalla
os.system('clear')

# Mostrem el mes de l'any
mostrarMes(mes, any)
