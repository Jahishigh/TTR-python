# On peut mettre ce qu'on veut dans un tableau
array = ["String", 5, True]
# Pour afficher tous le tableau :
print(array)
# Pour afficher une position précise dans le tableau (ici 5):
print(array[1])
# Pour afficher une position en partant de la fin (noter que la fin commence à -1) :
print(array[-1])
# Pour afficher à partir d'une position jusqu'à la fin :
print(array[1:])
# Pour afficher à partir d'une position jusqu'à une autre (n'inclue pas la position d'arrivé :
print(array[1:3])
# Pour modifier une valeur du tableau :
array[1] = "Nouvelle string"
print(array)
# Ajouter un tableau à la fin d'un autre tableau
second_array = ["Second Tableau", 42, False]
array.extend(second_array)
print(array)
# copier un tableau
new_array = array[:]
# Ajouter un élément à la fin de la liste
array.append("Nouvel élément")
# Ajouter un élément à une position précise (ce qui pousse les autres de 1 place
array.insert(1, "Element à la 2ième place")
# Enlever un élément du tableau
array.remove("Nouvelle string")
# Enlever le dernier élément du tableau
array.pop()
# Donne la position dans le tableau de l'élément en paramètre
array.index("String")
# Donne le nombre de fois que l'élément apparait dans le tableau
array.count("String")
# Ranger la liste dans l'ordre alphabétique ou croissant si c'est des int
array_to_sort = [3, 2, 8, 7]
array_to_sort.sort()
# Inverser l'ordre de la liste
array.reverse()
# Faire une copie d'une liste dans un nouveau tableau
copie_de_array = array.copy()
# Vider le tableau
array.clear()

# list unpacking
d, e, f, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # maintenant, d = 1, e = 2, f = 3, other = le reste
# si on rajouter une autre varible après other d,e,f, *other, g    g = 9 mais other = 45678
# si on rajoute une variable après other, il prend le dernier item
# unpack enleve la variable de la liste et la stock dans la variable


# Pour créer une liste 2D aussi appelé MATRIX, créer un tableau et mettez y plus de tableau pour un max de tableau
# Ceci crée donc une tableau où l'on voit les lignes et les colonnes, ce qui va servir à appeler les éléments
tableau_en_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Ici, on print l'élément ligne 0 colonne 0, donc l'élément 1
print(tableau_en_2d[0][0])