import os
import csv
import re
input("Pressez une touche pour créer un fichier regroupant toutes les inscriptions\n")

liste_fichiers = []

with open("inscrits_total.csv", "x", newline='') as new:
  ligne = csv.writer(new, delimiter=',')
  header = ["Prenom", "Nom", "Catégorie", "Adresse Mail"]
  ligne.writerow(header)

dossier = os.listdir(".")
for i in dossier:
  if re.match("inscrits-20", i):
    liste_fichiers.append(i)

new = open("inscrits_total.csv", "a")

for i in (liste_fichiers):
  temp = open(i, "r")
  for line in temp:
    new.write(line)
temp.close()
new.close()

input("Le fichier \"inscrits_total\" a bien été crée\nPressez une touche pour lancer la recherche et la suppression des doublons\n")

with open('inscrits_total.csv', 'r') as in_file, open('inscrits_total_v2.csv', 'w') as out_file:
  seen = set()
  for line in in_file:
    if line in seen or line=="\n": continue

    seen.add(line)
    out_file.write(line)

input("Doublons supprimés, une copie du fichier originale à été conservé.\nVous pouvez quitter cet utilitaire")


