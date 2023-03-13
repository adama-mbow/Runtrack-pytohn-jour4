#Écrire une fonction qui contient une liste nommée “fruits” qui contient les string
#“pomme”, “cerise”, “orange”.
#Affichez le 2e éléments de la liste.

def function():
    fruits = ["pomme", "cerise", "orange"]
    for fruit in fruits:
        return fruits[1]
    
print(function())