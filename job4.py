"""Écrire une fonction qui contient une liste nommée “fruits” qui contient les strings
“pomme”, “cerise”, “orange, Melon”. Cette fonction doit à son appel ajouter à la liste
“fruits” une String “Mangue” à l’index 2."""

def function():
    fruits = ["pomme", "cerise", "orange","Melon"]
    fruits.insert(2,"Mangue")
    return fruits
print(function())