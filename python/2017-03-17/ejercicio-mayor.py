# coding: utf-8

# Esperem a que l'usuari introdueixi el nombre 1
num1 = input("Nombre 1: ")

# Esperem a que l'usuari introdueixi el nombre 2
num2 = input("Nombre 2: ")

# Si el nombre 1 és més gran que el nombre 2
if (num1 > num2):
    print "Num 1 > Num 2"

# Si no ho és
else:

    # Si el nombre 2 és més gran que el nombre 1
    if (num1 < num2):
        print "Num 1 < Num 2"

    # Si no ho és (són iguals)
    else:
        print "Num 1 = Num2 "
