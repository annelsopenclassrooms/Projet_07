import csv
import pprint

import itertools

# Remplace 'fichier.csv' par le chemin de ton fichier CSV
nom_fichier = "actions3.csv"

# Liste pour stocker les dictionnaires
liste_dict = []

# Ouverture et lecture du fichier CSV
with open(nom_fichier, mode='r', encoding='utf-8') as fichier_csv:
    lecteur = csv.DictReader(fichier_csv)  # Utilise DictReader pour créer des dictionnaires
    for ligne in lecteur:
        liste_dict.append(dict(ligne))  # Convertit chaque ligne en dictionnaire et l'ajoute à la liste


#nettoyage des données du csv
for dict in liste_dict:
    profit = dict["Bénéfice (après 2 ans)"]
    profit = int(profit.strip('%'))
    dict['Bénéfice (après 2 ans)'] = profit

liste = ["A", "B", "C"]

comb = []
for n in range(1,len(liste)+1):
    comb.append([i for i in itertools.combinations(liste,n)])

print(comb)
print(len(comb))