# coding: utf-8

####################
##								##
## Néfix Estrada  ##
##								##
## Llegir Postgre ##
##								##
####################

# Imports
import os 
import sys
import psycopg2 # Llibreria per accedir al Postgre

#########
# Dades #
#########
database = "training"
user = "postgres"
db_password = "jupiter"


# ---------------- #
# Connexió a la DB #
# ---------------- #

# Intent
try:
	conn = psycopg2.connect(database = "training", user = "postgres", password = "jupiter") 

# Si hi ha un error
except: 
	print "Error al connectar amb la DB"
	print "Has arrencat el postgre?"
	print "Has modificat el fitxer 'pg_hba.conf' ?"
	exit(2)

# Declarem el "cur"
cur = conn.cursor()


#	--------------- #
# Mostrem el menú #
#	--------------- #

# Setejem la variable sortir a 0
sortir = 0

# Loop per sortir
while sortir != "1":

	# Netejem la pantalla
	os.system('clear')
	
	# Mostrem les opcions
	print "1- Llegir una taula"
	print "2- Sortir"
	print 

	# Esperem a que l'usuari trii una opció
	tria = raw_input('Siusplau, tria una opció: ')

	# Si ha triat "1"
	if tria == '1':

		#	--------------------------------- #
		# Llistem totes les taules de la DB #
		#	--------------------------------- #

		# Netejem la pantalla
		os.system('clear')
		
		# Executem una query que ens retorna totes les taules
		cur.execute("SELECT relname FROM pg_class WHERE relkind='r' AND relname !~ '^(pg_|sql_)';");
		tables = cur.fetchall()

		# Reinicialitzem el comptador a 1
		comptador = 1

		# Reinicialitzem el diccionari amb les taules
		dic_taules = {}
		dic_taules.clear()

		# Per cada taula
		for t in tables:

			# La transformem a string
			t = ''.join(t)

			# La afegim al diccionari
			dic_taules[comptador] = t

			# La mostrem
			print str(comptador) + "- " + t.title()

			# Augmentem el comptador
			comptador += 1


		# Esperem a que l'usuari trii una taula
		print
		tria_taula = raw_input("Siusplau, tria una taula: ")

		# Transformem la tria a un int
		tria_taula = int(tria_taula)

		# Si la opció seleccionada existeix al diccionari
		if dic_taules.has_key(tria_taula):

			# Intentem executar la query
			try:

				#	--------------------- #
				# Començem amb la query #
				#	--------------------- #

				# Query 
				cur.execute("SELECT * FROM " + dic_taules[tria_taula]);

				#	------------------------------------------------------------------------------------- #
				# Llistem totes les columnes de la taula i ho afegim al fitxer auxiliar com a capçalera #
				#	------------------------------------------------------------------------------------- #
				
				# Llistem les columnes
				rows = cur.fetchall()
				colnames = [desc[0] for desc in cur.description]

				# Guardem la capçalera de la taula
				capsalera = ''

				# Per cada caràcter a 'colnames'
				for c in colnames:

					# Si és l'ultima columna
					if c == colnames[-1]:
						capsalera += c
					
					# Si no és l'última li afegeix el separador de ':'
					else:
						capsalera += c + ':'

				# Ho guaredem al fitxer 'sql_query.txt' (com a línia nova)
				os.system('echo ' + capsalera + '>> sql_query.txt')

				#	-------------------------------------------------------------------------------- #
				# Creem un separador entre la capçalera i les dades i ho afegim al fitxer auxiliar #
				#	-------------------------------------------------------------------------------- #

				# Creem la línia  entre la capçalera i les dades
				separador_capsalera = ''

				# Per cada caràcter a 'capsalera'
				for c in capsalera:

					# Si és un separador, el mantenim
					if c == ":":
						separador_capsalera += ':'

					# Si no és un separador, el convertim a '-' 
					else:
						separador_capsalera += '-'

				# Ho guaredem al fitxer 'sql_query.txt' (com a línia nova)
				os.system('echo ' +  separador_capsalera + ' >> sql_query.txt')

				#	----------------------------------- #
				# Afegim les dades al fitxer auxiliar #
				#	----------------------------------- #

				# Definim la variable resultat_rows
				resultat_rows = 'resultat = '

				# Definim la variable del total de columnes menys 1
				cols_rang = len(colnames)

				# Definim la variable del comptador pel següent loop
				comptador_cols = 0

				# Loop per crear la variable 'resultat'
				while comptador_cols != cols_rang:

					# Si és igual que 0
					if comptador_cols == cols_rang - 1:
						resultat_rows = resultat_rows + 'str(row[' + str(comptador_cols) + '])'

						comptador_cols = comptador_cols + 1

					# Si no és igual a 0
					else:
						resultat_rows = resultat_rows + 'str(row[' + str(comptador_cols) + ']) + ":" +'

						comptador_cols = comptador_cols + 1

				# Per cada entrada a la taula
				for row in rows:

						# Executem l'string 'resultat_rows'
						exec(resultat_rows)

						# Ho guaredem al fitxer 'sql_query.txt' (com a línia nova)
						os.system('echo ' + resultat + ' >> sql_query.txt')

				# Netejem la pantalla
				os.system('clear')

				#	------------------------- #
				# Mostrem el resultat final #
				#	------------------------- #

				# Mostrem el nom de la taula
				print dic_taules[tria_taula].title()

				# Mostrem un espai en blanc per separar el títol de la taula de les dades
				print

				# Mostrem el resultat
				os.system('column -t -s":" sql_query.txt')

				# Esborrem el fitxer auxiliar
				os.system('rm sql_query.txt')

				# Mostrem dos espais en blanc per separar la informació del raw_input
				print
				print

				# Esperem a que l'usuari vulgui continuar
				esperar = raw_input("Prém una tecla per continuar...")


			#	---------------------------- #
			# Control d'errors del postgre #
			#	---------------------------- #

			# Si hi ha un error
			except psycopg2.Error as er:

				# Mostra per pantalla l'error
				print er.pgcode

				# Tanca la connexió amb la DB
				conn.rollback()


		#	---------------------------- #
		# Control d'errors de selecció #
		#	---------------------------- #

		# Si la opció seleccionada NO existeix al diccionari
		else:

			# Netejem la pantalla
			os.system('clear')

			# Mostrem per pantalla un "error"
			print "Siusplau, tria una opció correcta"
			
			# Esperem 2 segons
			os.system('sleep 2')
			
	#	------------------ #
	# Sortida del script #
	#	------------------ #

	# Si ha triat "2"
	elif tria == '2':

		# Netejem la pantalla
		os.system('clear')

		# Sortim
		sortir = "1"

	#	---------------------------- #
	# Control d'errors de selecció #
	#	---------------------------- #

	# Si ha triat una altra cosa
	else:

		# Netejem la pantalla
		os.system('clear')

		# Mostrem per pantalla un "error"
		print "Siusplau, tria una opció correcta"
		
		# Esperem 2 segons
		os.system('sleep 2')

# ---------------------------- #
# Tancar la connexió amb la DB #
# ---------------------------- #
conn.close()