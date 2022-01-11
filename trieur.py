import os
import csv
import re

# chercher les fichiers commencant par "inscrits" OK
# ouvrir le 1er
#   copier chaque ligne
#   ouvrir le inscrits_total et copier dedans
# ouvrir le second
#   copier chaque ligne
#   ouvrir le inscrits_total et copier dedans
# etc

liste_fichiers = []

with open("inscrits_total.csv", "x") as f:
  ligne = csv.writer(f, delimiter=',')
  header = ["Prenom", "Nom", "Catégorie", "Adresse Mail"]
  ligne.writerow(header)


dossier = os.listdir(".")
for i in dossier:
  if re.match("inscrits-20", i):
    liste_fichiers.append(i)

print(liste_fichiers)








