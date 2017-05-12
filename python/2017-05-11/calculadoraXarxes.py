# coding: utf-8

# Treballarem amb str perquè hi hagin els zeros correctes

# Canvi a binari
def nombreBinari(nombre):

    # Llista amb els digits
    binari = []

    # Mentres el nombre encara es pot dividir
    while (nombre >= 2):

        # Guardem el residu de la divisió
        binari.append(nombre % 2)

        # Dividim el nombre entre 2 (enter)
        nombre = nombre // 2

    # Afegim l'últim nombre a la llista
    binari.append(nombre)

    # Transformem la llista al revés
    binari = list(reversed(binari))

    # Ho convertim tot a str i ho ajuntem a un únic str
    binari = ''.join(map(str, binari))

    # Ho transformem a int i ho retornem
    return int(binari)

# Canvi a decimal
def nombreDecimal(nombre):

    # Definim la variable llistaNombre (una llista que és )
    llistaNombre = []

    # Per cada digit al nombre, afegeix-lo a la llista
    for x in str(nombre):

        # Afegeix el nombre a la llista
        llistaNombre.append(int(x))

    # Definim la variable nombre decimal i el comptador
    nombreDecimal = 0
    count = 1

    # Per cada item a la llista, fes la conversió
    for i in llistaNombre:

        # Mirem quin nombre hem d'elevar
        posicio = ((len(llistaNombre)) - count)

        # Fem la conversió i ho afegim al nombre anterior
        nombreDecimal = nombreDecimal + (i * (2 ** posicio))

        # Augmentem el count
        count = count + 1

    # Retornem el nombre en decimal
    return nombreDecimal


# Canviem la ip de xarxa i la màscara de xarxa a binari
def ipMascaraXarxaBinari(ip, mascara):

        # Transformem la ip de xarxa a octets
        ip = map(int, ip.split('.'))

        # Inicialitzem la variable de la màscara a binari
        ipBinari = []

        # Per cada octet, el transformem a binari
        for octet in ip:

            # Transformem l'octet a binari
            ipBinari.append(str(nombreBinari(octet)).zfill(8))

        # Transformem la màscara de xarxa a octets
        mascara = map(int, mascara.split('.'))

        # Inicialitzem la variable de la màscara a binari
        mascaraBinari = []

        # Per cada octet, el transformem a binari
        for octet in mascara:

            # Transformem l'octet a binari i l'afegim a la llista en format str amb un mínim de caràcters (perquè sigui 00000100)
            mascaraBinari.append(str(nombreBinari(octet)).zfill(8))

        # Retornem la ip de xarxa en binari i la màscara de xarxa en binari
        return ipBinari, mascaraBinari

# Calculem quants bits de host té la màscara
def bitsHost(mascara):

    # Ajutem tota la màscara en un sol string
    binari = ''.join(mascara)

    # Definim la variable zeros
    zeros = 0

    # Per cada digit, mirem si és un 0 i si ho és ho afegim a la variable zeros
    for digit in binari:

        # Mirem si és un 0
        if (digit == '0'):

            # Augmentem la variable zeros
            zeros = zeros + 1


    # Retornem quants bits de host hi ha
    return zeros

# Calculem la direcció de broadcast
def ipBroadcast(xarxa, mascara):

    # Mirem quants bits de host hi ha
    bitsHostNum = bitsHost(mascara)

    # Generem els uns necessaris per transformar la ip de xarxa a una ip de broadcast
    bitsBroadcast = ''
    for i in xrange(0,bitsHostNum):
        bitsBroadcast = bitsBroadcast + '1'

    # Ajuntem tota la màscara en un sol string
    ip = ''.join(xarxa)

    # Canviem els últims bits de la ip a uns per transformar-ho a la ip de broadcast
    ip = ip[:-bitsHostNum] + bitsBroadcast

    # Definim la variable octet
    octet = ''

    # Definim la variable ipBroadcast
    ipBroadcastBinari = []

    # Separem el nou nombre a una llista
    for x in str(ip):

        # Afegim el nombre a l'octet
        octet = octet + x

        # Si l'octet és de 8
        if (len(octet) == 8):

            # Afegim l'octet a la ip de broadcast
            ipBroadcastBinari.append(octet)

            # Resetejem la variable octet
            octet = ''



    # Transformem la ip a decimal
    for i in ipBroadcastBinari:

        # Transformem l'octet a decimal i l'afegim al resultat final
        ipBroadcast = str(nombreDecimal(i)) + '.'

    # Retornem la ipBroadcast
    return ipBroadcast

# Mapejem la xarxa
def mapejarXarxa(ipXarxa, mascaraXarxa):

    # Convertim les ip a binari
    ipXarxaBinari, mascaraXarxaBinari = ipMascaraXarxaBinari(ipXarxa, mascaraXarxa)

    print ipXarxaBinari

    # Agafem l'últim caràcter de la ip de xarxa, li sumem 1 i ho ajuntem a la ip sencera sense la part modificada
    primeraHostUtil = ipXarxa[:(len(ipXarxa)) - 1] + str(int(ipXarxa[-1]) + 1)

    #

    # Mirem quants bits de host hi ha, elevem 2 a aquest nombre i li restem 2 (la direcció de xarxa i de broadcast)
    hostsUtils = str(2 ** int(bitsHost(mascaraXarxaBinari)) - 2)



    print "Ip xarxa: " + ipXarxa
    print "Ip broadcast: " + ipBroadcast(ipXarxa, mascaraXarxa)
    print "Primera direcció de hosts útil: " + primeraHostUtil
    print "Última direcció de hosts útil: "
    print "Hosts útils: " + hostsUtils



mapejarXarxa('192.168.1.0', '255.255.255.0')
