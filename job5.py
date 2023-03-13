"""Écrire un programme qui créé une liste nommée “L” d’au moins 5 entiers puis
successivement :
- Afficher la valeur de L[1]
- Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
- Puis afficher la valeur du dernier terme de la liste."""

def function():
    L = [1,2,3,4,5]
    print(L)
    print (L[1])
    NL3 = L[2] + L[4]
    L[3] = NL3
    print(L)
function()