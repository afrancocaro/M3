# coding: utf-8

# Importem les funcions del sistema
import os

# Netejem la pantalla
os.system('clear')

# Esperem a que l'usuari ens retorni l'edat
edat = raw_input("Quants anys tens? ")

# Si el text és un nombre
if edat.isdigit():
	
  edat = int(edat)

  # Si té entre 18 i 23 anys o 17
  if (((edat >= 18) and (edat <= 23)) or (edat == 17)):

    # Mostra per pantalla que pot entrar
    print "Pots entrar!!"

    # Si és massa petit
  elif (edat < 17):

    # Mostra per pantalla que no pot entrar
    print "Ets massa jove per entrar!!"

  # Si és massa gran
  else:

    # Mostra per pantalla que no pot entrar
    print "Ets massa vell per entrar!!"

# Si no és un nombre enter
else:

  # Mostrem per pantalla un text d'error
  print "Siusplau, introdueix una opció correcta"
