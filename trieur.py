import os
import csv
test = "boloss"
print(test[:3])

# def add_ligne(nom_fichier, liste_info):
#     if not nom_fichier in os.listdir("."):
#         entete = True
#     else:
#         entete = False
#     with open(nom_fichier, "a") as fichier:
#         ligne = csv.writer(fichier, delimiter=',')
#         if entete == True:
#             header = ["Prenom", "Nom", "Catégorie", "Adresse Mail"]
#             ligne.writerow(header)
#         ligne.writerow([liste_info[0],liste_info[1], liste_info[3], liste_info[4]

# target = os.listdir().count("inscrits")
# print(target)
#
# t=0
# for _ in os.listdir():
#     if "inscrits" in os.listdir():
#         t += 1
# print(t)

nbr=0
# target = os.listdir()
for i in os.listdir():
  if "inscrits" in i:
    nbr += 1

print(nbr)

doublon = 0
for i in range(nbr):
    f[i] = open("inscrits", "r")
    lecture = f[i].readlines()
    for _ in lecture:
        f[i+1] = open("inscrits", "r")
        lecture2 = f[i+1].readlines()
        if lecture == lecture2:
            doublon += 1
print(doublon)


