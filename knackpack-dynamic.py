# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 



import csv
import pprint

import itertools
import time



def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] 
							+ K[i-1][w-wt[i-1]], 
							K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 

	return K[n][W] 


# Driver code 
if __name__ == '__main__': 
	


    start_time = time.time()

    profit = [100,300,750,1400,1020,2000,154,286,624,918,714,990,874,14,54,64,48,140,504,2052]
    weight = [20,30,50,70,60,80,22,26,48,34,42,110,38,14,18,8,4,10,24,114] 
    W = 500
	
    n = 20
    print(knapSack(W, weight, profit, n)) 




    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Temps d'exécution : {execution_time:.6f} secondes")
# This code is contributed by Bhavya Jain 

