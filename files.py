import datetime
import csv

def date():
    date_enregistrement = datetime.date.today()
    return date_enregistrement

def add_ligne(nom_fichier, liste_info):
    with open(nom_fichier, "a", newline='') as fichier:
        for i in liste_info:
            csv.writer(fichier, str(i), delimiter=',')
        fichier.write("\n")


