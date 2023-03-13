"""Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste
L = [8, 24,48,2,16]"""

def multiple():
    L = [8, 24,48,2,16]
    L3 = []
    for i in L:
        if i % 3 == 0:
            L3.append(i)
            print(L3)
            print(len(L3))
    
(multiple())