# coding: utf-8

# Inicialitzem les variables necessàries pel bucle
sortir = False
count = 0

# Bucle que compta de 0 a 3
while (sortir == False):

    # Mosta el nombre actual
    print count

    # Si el nombre és 3, parem de comptar
    if (count == 3):

        # Parem de comptar (acabem el loop)
        sortir = True

    # Augmentem en 1 el comptador
    count = count + 1
