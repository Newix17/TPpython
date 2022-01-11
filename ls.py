import argparse
import os

browser = argparse.ArgumentParser()
browser.add_argument("-f", "--finder", type=str, help="affiche les fichiers et dossiers d'un répertoire donné" )
path = browser.parse_args()

if path.finder:
    print(path.finder, os.listdir(path.finder))