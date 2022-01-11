import argparse

createur = argparse.ArgumentParser()
createur.add_argument("-n", "--nommeur", type=str, help="crée et nomme un fichier.txt du nom donné en argument, je cois")
go = createur.parse_args()

if go.nommeur:
    with open(go.nommeur, "x") as f:
        f.close()
