#!/usr/bin/env python3

import sys 

current_word = None
current_count = 0
word = None

# lire la ligne entière de STDIN (l'entree) 
for line in sys.stdin: 
	# supprimer les espaces blancs de début et de fin 
	line = line.strip() 
	# fractionner les données sur la base de tabulation que nous avons fourni dans mapper.py
	word, count = line.split('\t', 1) 
	# convertir count (actuellement une chaîne) en int 
	try: 
		count = int(count) 
	except ValueError: 
		# le nombre n’était pas un nombre, donc silencieusement 
		# ignorer/supprimer cette ligne 
		continue

	#cette commutation IF ne fonctionne que parce que Hadoop trie la sortie de la carte 
	# par clé (ici : mot) avant d'être transmis au reducer 
	if current_word == word: 
		current_count += count 
	else: 
		if current_word: 
			# Afficher les résultats à la sortie standard
			print(current_word, '\t', current_count) 
			
		current_count = count 
		current_word = word 

# Afficher le dernier mot si necessaire 
if current_word == word: 
	print(current_word, '\t', current_count) 

