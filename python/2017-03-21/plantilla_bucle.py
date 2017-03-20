# coding: utf-8

# Assignem a "false" la variable per soritr
sortir = False

# Loop (mentres sortir sigui fals)
while (sortir == False):

    # Mostrem per pantalla "Hola"
    print "Hola"

    # Esperem a que l'usuari vulgui continuar o sortir
    tecla = raw_input()

    # Si vol sortir
    if ((tecla == "s") or (tecla == "S")):

        # Mostrem per pantalla "adios"
        print "Adios"

        # Assignem a "true" la variable sortir
        sortir = True
