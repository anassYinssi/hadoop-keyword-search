#!/usr/bin/env python3
  
# importer le module sys car nous devons lire et écrire des données dans STDIN et STDOUT 
import sys 

#Définir la liste des mots-clés à rechercher dans chaque ligne d'entrée
keywords=["the","fantasy","mystery","horror","hero","protagonist","flashback","love","conflict","friendship"]
# reading entire line from STDIN (standard input) 
for line in sys.stdin: 
    # Supprime les espaces inutiles en début et fin de ligne
    line = line.strip() 
    # Divise la ligne en mots
    words = line.split() 
      
    # On boucle sur la liste words pour afficher les occurences de nos mots-clés   
    # avec un STDOUT de 1 pour chaque occurence 
    for word in words: 
        # inscrire les résultats dans STDOUT (sortie standard) 
        # ce que nous produisons ici sera l’entrée 
        # pour l'etape de reduce, c.-à-d l’entrée pour reducer.py  
        if(word in keywords):
            print(word, '\t',1)