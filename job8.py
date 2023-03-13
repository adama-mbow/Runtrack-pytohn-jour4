"""Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]"""

def paire():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    L1 = []
    for i in L:
        if i % 2 == 0:
            L1.append(i)
    print(L1)
    somme = sum(L1)
    print(somme)
        
paire()