"""
 Held-Karp algorithm for Traveling Salesperson Problem
 """


import itertools
from itertools import combinations, chain
import sys #for sys.maxint - representing a maximum integer size in Python


def travel(n, G):
    D  = [{} for x in range(n)] #each vertex has a dictionary of subsets
    P = [{} for x in range(n)] #each vertex has a dictionary of subsets
    for i in range(1,n,1):
       D[i][frozenset()]=G[i][0]
       P[i][frozenset()]=0

    for k in range(1,n-1,1):
        size_k_subsets = generate_subsets(set(range(1,n,1)), k )
        for A in size_k_subsets:
            X = {i for i in range(n)} # X contains the vertices that are not v0 and aren't in A
            X= X-A
            X=X-{0}
            
            for i in X:
                def dist_via(u):
                    if frozenset(A - {u}) in D[u]:
                        return G[i][u] + D[u][frozenset(A - {u})]
                    else: 
                        return sys.maxsize
                
                #The list of things in X sorted by that criterion.
                sorted_by  = sorted(list(A), key = dist_via)
                

                minValSorted=sorted_by[0]
                D[i][frozenset(A)]=G[i][minValSorted]+D[minValSorted][frozenset(A - {minValSorted})]
                P[i][frozenset(A)]=minValSorted 

                

    #Same idea as the loop above, except ONLY with the first vertex

    def dist_via_fin(u):
        if frozenset(set(range(n)) - frozenset({0, u})) in D[u]:
            return G[0][u]+D[u][frozenset(set(range(n)))-frozenset({0, u})]
        else: 
            return sys.maxsize
    
    sorted_by  = sorted(list(range(1,n,1)),key = dist_via_fin)
    j = P[0][frozenset(set(range(n))-{0})] = sorted_by[0] 
    min_length = D[0][frozenset(set(range(n))-{0})] = G[0][j] + D[j][frozenset(set(range(n)) - {0,j})]
    tour = get_opt_tour(P,j,n) #Retrieve the tour itself
    return min_length , tour

""" Retrieve the optimal tour from P: work backwards through P. 
Note this relies on us knowing the last j value at the end of the main algorithm above."""
def get_opt_tour(P,j,n):
    
    X=frozenset(range(1,n))-{0}
    tour = [0]
    val=j
    tour.append(val)
    while(len(tour)<n+1):
        #val is the optimal tour vertex
        X=X-{val}
        val=P[val][X-{val}]
        tour.append(val)
        
    
    return tour

""" Generate all the size k subsets of Y """
def generate_subsets(Y, k):
    return list(map(set, itertools.combinations(Y, k)))


dist = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]


min_cost, opt_tour = travel(len(dist), dist)
print("Optimal tour length:", min_cost)
print("Optimal tour:", opt_tour)


#prints 
# Optimal tour length: 80
# Optimal tour: [0, 1, 3, 2, 0]



"""
dist = [[0, 15, 20, 25],
        [15, 0, 40, 30],
        [20, 40, 0, 35],
        [25, 30, 35, 0]]
min_cost, opt_tour = travel(len(dist), dist)
print("Optimal tour length:", min_cost)
print("Optimal tour:", opt_tour)
"""

#prints 
# Optimal tour length: 100
# Optimal tour: [0, 1, 3, 2, 0]

