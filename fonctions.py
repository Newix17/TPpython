#Rédaction des fonctions :

#_____________________________________________________________
#Insertion du nom, prénom, et année de naissance
def inser(n,pn,y):
    n, pn, y = input("indiquez le Nom, Prénom et année de naissance, séparés par un espace\n").split(" ")
    y = int(y)

#_____________________________________________________________
# Génération des adresses Mails :
# Premiere lettre du Prénon suivie d'un point et du nom complet
# Vient l'arobase et baton-rouge.fr

#_____________________________________________________________
#Attribution des catégories
#définies par l'âge, lui-même défini par l'année de naissance.