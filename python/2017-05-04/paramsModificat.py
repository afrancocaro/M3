# coding:utf-8

# PARAMETROS
# ---------------------------------------------------------------
# nombre          : entrada          valor       no modificable
# apellido1       : entrada/salida   referencia  modificable
# apellido2       : entrada/salida   referencia  modificable
# nombre_completo : salida           referencia  modificable
# ---------------------------------------------------------------
def mensaje_bienvenida(nombre, apellido1, apellido2):
	print "*****************************"
	print "          BIENVENIDO         "
	print " ", nombre , "," , apellido1, "," , apellido2
	print "*****************************"

	nombre_completo=nombre+","+apellido1+" "+apellido2

	nombre="CAMBIO"
	apellido1="CAMBIAZO"
	apellido2="CAMBIAZON"



	return apellido1,apellido2,nombre_completo

#############################################################################

nombre="PEPE"
apellido1="SANCHEZ"
apellido2="LOPEZ"
nombre_completo=""

print nombre , apellido1, apellido2,nombre_completo


# ----------------------------------------------------------------------
# nombre          : entrada          valor       no modificable
# apellido1       : entrada/salida   referencia  modificable
# apellido2       : entrada/salida   referencia  modificable
# nombre_completo : salida           referencia  modificable
# ----------------------------------------------------------------------
apellido1,apellido2,nombre_completo=mensaje_bienvenida(nombre,apellido1,apellido2)


# Sólo cambia el valor de los parámetro modificables
print nombre , apellido1, apellido2,nombre_completo
