import datetime
import fonctions
import files

poussin=[]
cadet=[]
junior=[]
semipro=[]
pro=[]
print("Bonjour, Bienvenue dans l'assistant d'inscription au Club de Quidditch v1.0\n")

encore = True
while encore:
    liste = []
    nom = input("Veuillez saisir le NOM du joueur:\n")
    prenom = input("Et son PRENOM:\n")

    continuer = True
    while continuer:
        birth = input("Pour finir la saisie, merci d'entrer son année de naissance:\n")
        result = fonctions.check_year(birth)
        if result:
            continuer = False
        else:
            continuer = True

        try:
            birth = int(birth)
        except ValueError:
            print("Merci d'indiquer l'année en chiffres")

        if birth > 2022 or birth < 1922:
            print("Saisie non valide")
            continuer = True
        else:
            continuer = False


    if fonctions.category(birth) == "Poussin":
        poussin.append(nom)
    if fonctions.category(birth) == "Cadet":
        cadet.append(nom)
    if fonctions.category(birth) == "Junior":
        junior.append(nom)
    if fonctions.category(birth) == "Semi-Pro":
        semipro.append(nom)
    if fonctions.category(birth) == "Pro":
        pro.append(nom)

    liste.append(prenom)
    liste.append(nom)
    liste.append(birth)
    liste.append(fonctions.category(birth))
    email = fonctions.mail(prenom,nom)
    liste.append(email)

    print(f"Félicitations, vous avez inscrit", (prenom),(nom), "il jouera dans la catégorie",(fonctions.category(birth)))
    print("Sa nouvelle adresse mail est :",(email),)

    date_enregistrement = files.date()

    nom_fichier = "inscrits-"+str(date_enregistrement)+".csv"

    files.add_ligne(nom_fichier, liste)


    continuer = True
    while continuer:
            again = input("Voulez-vous enregister un(e) autre joueur(euse)? o/n?")
            if again == "n":
                encore = False
                continuer = False
            elif again == "o":
                encore = True
                continuer = False
            else:
                print("Saisie non reconnue")
                encore = False
                continuer = True
print("Vous avez terminé vos enregistrements")






