import fonctions
import files
liste=[]
poussin=[]
cadet=[]
junior=[]
semipro=[]
pro=[]
print("Bonjour, Bienvenue dans l'assistant d'inscription au Club de Quidditch v1.0\n")

encore = True
while encore:

    nom = input("Veuillez saisir le NOM du joueur:\n")
    prenom = input("Et son PRENOM:\n")

    continuer = True
    while continuer:
        birth = input("Pour finir la saisie, merci d'entrer son année de naissance:\n")
        try:
            birth = int(birth)
        except ValueError:
            print("Merci d'indiquer l'année en chiffres")
        except:
            if birth > 2022 or birth < 1922:
                print("Saisie non valide")
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
print("Vous avez terminé vos enregistrements, appuyez sur Alt+F4")


