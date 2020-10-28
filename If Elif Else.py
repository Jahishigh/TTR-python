# Permet de donner des conditions au code pour effectuer un code à un certain moment ou dans certain cas
# Ici, if vérifie si la variable cest_vrai est True, si c'est le cas, le print s'effectue
# Si cest_vrai est False, alors le code entre dans le else
cest_vrai = True
if cest_vrai:
    print("C'était bien vrai")
else:
    print("C'était pas vrai")
# if permet de vérifier plusieurs condition à la fois
# Ici or permet de vérifier si l'un ou l'autre est True, alors le code entre dans le if
cest_vrai = True
cest_beau = True
if cest_vrai or cest_beau:
    print("C'était bien vrai et beau")
# Ici and permet de vérifier si les deux sont True
cest_vrai = True
cest_beau = True
if cest_vrai and cest_beau:
    print("C'était bien vrai et beau")
# elif permet d'ajouter un nouveau cas de condition possible après un premier if
# not(variable) permet de vérifier si une varible est False
cest_vrai = True
cest_beau = False
if cest_vrai and cest_beau:
    print("C'était bien vrai et beau")
elif cest_vrai and not cest_beau:
    print("C'est vrai mais c'est pas beau")
# if permet aussi de comparer des chiffres par exemple
# Type de comparaison : > < >= <= != ==
if 5 < 6:
    print("C'était évident")
# Ou comparer des string
if "ceci" == "ceci":
    print("Ceci est bien ceci")