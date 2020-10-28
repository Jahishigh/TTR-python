# for prend une condition en variable, à chaque passage de la loop la variable va changer jusqu'à arriver à la condition
# la variable après le for peut avoir n'importe quel nom, c'est la condition final qui compte
for letter in "Hello":
    print(letter)

list_de_value = [1, 2, 3]
for value_in_list in list_de_value:
    print(value_in_list)

for chiffre in range(6):
    print(chiffre)
# Si on reprend l'exemple de notre liste 2d (voir plus haut)
# Ici on affiche tous le tableau 2d
tableau_en_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for ligne in tableau_en_2d:
    print(ligne)
# Ici on print chaque élément individuelement
for ligne in tableau_en_2d:
    for colonne in ligne:
        print(colonne)