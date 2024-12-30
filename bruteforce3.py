import csv
import pprint

import itertools
import time

start_time = time.time()

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

# liste = ["A", "B", "C"]

# comb = []
# for n in range(1,len(liste_dict)+1):
#     comb.append([i for i in itertools.combinations(liste_dict,n)])

# print(comb)
# print(len(comb))


comb = []
for n in range(1, len(liste_dict) + 1):
    for i in itertools.combinations(liste_dict, n):
        sum = 0
        earning = 0
        dict_comb = {}
        for j in i:
            earning = earning + (int(j['Coût par action (en euros)']) * int(j['Bénéfice (après 2 ans)'])/ 100)
            sum = sum + int(j['Coût par action (en euros)'])
            #print(j['Coût par action (en euros)'])
        # print(i)
        print(sum)
        # print(f"earning: {earning}")
        if sum <= 500:
            #print("added")
            dict_comb["combinaison"] = i
            dict_comb["earning"] = earning
            dict_comb["sum"] = sum
            comb.append(dict_comb)

        # else:
        #     #print('not added')

# print(len(comb))
# for i in comb:
#     print(i["combinaison"])
#     print(i["earning"])
#     print(i["sum"])

# Trier la liste de dictionnaires par "earning" en ordre décroissant
comb_sorted = sorted(comb, key=lambda x: x["earning"], reverse=True)

print (comb_sorted[0]["combinaison"])
print (comb_sorted[0]["earning"])


end_time = time.time()

execution_time = end_time - start_time
print(f"Temps d'exécution : {execution_time:.6f} secondes")