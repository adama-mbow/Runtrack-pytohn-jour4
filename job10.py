"""Écrire un programme qui calcule le produit de toutes les valeurs de la liste comprises
dans l’intervalle [25, 90]
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]"""

def produit():
    L =[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    P=[]
    for i in L:
        if i >= 25 and i <=90:
            P.append(i)
    print(P)
    produits = 1
    for j in P:
        produits = produits * j
    print (produits)
    
produit()
  
