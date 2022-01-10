import datetime
import csv
import os

def date():
    date_enregistrement = datetime.date.today()
    return date_enregistrement

def add_ligne(nom_fichier, liste_info):
    if not nom_fichier in os.listdir("."):
        entete = True
    else:
        entete = False
    with open(nom_fichier, "a") as fichier:
        ligne = csv.writer(fichier, delimiter=',')
        if entete == True:
            header = ["Prenom", "Nom", "Catégorie", "Adresse Mail"]
            ligne.writerow(header)
        ligne.writerow([liste_info[0],liste_info[1], liste_info[3], liste_info[4]])




path = os.listdir(".")
print(path)

if "fonctions.py" in path:
    print("ok")
else:
    print("nok")