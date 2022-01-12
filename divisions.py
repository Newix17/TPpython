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
        print(line)
        # if re.match("Poussin", line):
        #     poussin.append(line[1])
        # if re.match("Cadet", line):
        #     cadet.append(line[1])
        # if re.match("Junior", line):
        #     junior.append(line[1])
        # if re.match("Semi-Pro", line):
        #     semipro.append(line[1])
        # if re.match("Pro", line):
        #     pro.append(line[1])
        # else:
        #     non_admis.append(line)

print("Poussin:",(poussin),"\n","Cadet:",(cadet),"\n","Junior:",(junior),"\n","Semi-Pro:",(semipro),"\n","Pro:",(pro),"\n","Non Admis:",(non_admis),"\n",sep="")


