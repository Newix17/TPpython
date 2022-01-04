#corps du code
def inser(n,pn,y):
    n, pn, y = input("indiquez le Nom, Prénom et année de naissance, séparés par un espace\n").split(" ")
    y = int(y)

def initiale(prenom):
    i = prenom
    return i[0]

def mail(prenom,nom):
    adresse = initiale(prenom),".",nom,"@baton-rouge.fr"
    return adresse

print(mail("Guy","Pasdebol"))