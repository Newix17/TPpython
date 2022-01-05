def initiale(prenom):
    i = prenom
    return i[0]

def mail(prenom,nom):
    adresse = initiale(prenom),".",nom,"@baton-rouge.fr"
    return adresse

def category(birth):
    cat = 0
    age = 2022 - birth
    if age < 6 or age > 40:
        cat = "Non admis"
    elif age >= 6 and age < 12:
        cat = "Poussin"
    elif age >= 12 and age < 18:
        cat = "Cadet"
    elif age >= 18 and age < 24:
        cat = "Junior"
    elif age >= 24 and age < 30:
        cat = "Semi-Pro"
    elif age >= 30 and age < 40:
        cat = "Pro"
    return cat
