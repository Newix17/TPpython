
non_admis=[]
poussin=[]
cadet=[]
junior=[]
semipro=[]
pro=[]


with open("inscrits_total_v2.csv", "r") as f:
    for line in f:

        ligne = [x for x in line[:-2].split(",")]
        if "Poussin" in ligne[2]:
            poussin.append(ligne[0])
        if "Cadet" in ligne[2]:
            cadet.append(ligne[0])
        if "Junior" in ligne[2]:
            junior.append(ligne[0])
        if "Semi-Pro" in ligne[2]:
            semipro.append(ligne[0])
        if "Pro" in ligne[2]:
            pro.append(ligne[0])
        if "Non admis" in ligne[2]:
            non_admis.append(ligne[0])
        else:
            pass

print("La categorie POUSSIN contient:",(len(poussin)),"personne(s):")
for i in poussin:
    print(i)
print("La categorie CADET contient:",(len(cadet)),"personne(s):")
for i in cadet:
    print(i)
print("La categorie JUNIOR contient:",(len(junior)),"personne(s):")
for i in junior:
    print(i)
print("La categorie SEMI-PRO contient:",(len(semipro)),"personne(s):")
for i in semipro:
    print(i)
print("La categorie PRO contient:",(len(pro)),"personne(s):")
for i in pro:
    print(i)
print("La categorie NON ADMISSIBLE contient:",(len(non_admis)),"personne(s):")
for i in non_admis:
    print(i)
