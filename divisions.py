# from main import *
import re
import csv

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
            poussin.append(ligne[1])
        if "Cadet" in ligne[2]:
            cadet.append(ligne[0])
            cadet.append(ligne[1])
        if "Junior" in ligne[2]:
            junior.append(ligne[0])
            junior.append(ligne[1])
        if "Semi-Pro" in ligne[2]:
            semipro.append(ligne[0])
            semipro.append(ligne[1])
        if "Pro" in ligne[2]:
            pro.append(ligne[0])
            pro.append(ligne[1])
        if "Non admis" in ligne[2]:
            non_admis.append(ligne[0])
            non_admis.append(ligne[1])
        else:
            pass

print("Poussin:",(poussin),"\n","Cadet:",(cadet),"\n","Junior:",(junior),"\n","Semi-Pro:",(semipro),"\n","Pro:",(pro),"\n","Non Admis:",(non_admis),"\n",sep="")


