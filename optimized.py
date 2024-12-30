# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 



import csv
import pprint

import itertools
import time


def knapSack(W, wt, val, names, n): 
    # Initialisation de la table K
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Remplissage de la table en programmation dynamique
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w]
    
    # Récupération des objets inclus dans la solution optimale
    w = W
    selected_items = []

    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:  # L'objet i a été inclus
            selected_items.append(names[i - 1])  # Ajouter le nom de l'objet
            w -= wt[i - 1]

    return K[n][W], selected_items



# Driver code 
if __name__ == '__main__': 
	


    start_time = time.time()

    # Initialisation des listes vides
    names = []
    value = []
    profit = []

    # Remplace 'fichier.csv' par le chemin de ton fichier CSV
    nom_fichier = "Liste+d'actions+-+P7+Python+-+Feuille+1.csv"

    # Ouverture et lecture du fichier CSV
    with open(nom_fichier, mode='r', encoding='utf-8') as fichier_csv:
        reader = csv.DictReader(fichier_csv)  # Utilise DictReader pour créer des dictionnaires
            
        # Parcours des lignes du CSV
        for row in reader:
            names.append(row['Actions #'])
            value.append(int(row['Coût par action (en euros)']))
            # Calcul du profit : (Coût * Bénéfice) / 100
            profit.append(int(row['Coût par action (en euros)']) * int(row['Bénéfice (après 2 ans)'].strip('%')))



    W = 500
    n = len(value)
    print(knapSack(W, value, profit, names, n))




    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Temps d'exécution : {execution_time:.6f} secondes")
# This code is contributed by Bhavya Jain 

