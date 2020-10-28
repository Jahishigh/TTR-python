# Permet de mettre des bouts de code dans une fonction, et appeler cette fonctions plusieurs fois
# sans devoir reécrire tous le code à chaque fois
# Pour créer une fonction :
# les parenthèses après le nom de la fonction sont pour passer des paramètres
# Dans cette fonction, je dois donner 2 paramètres : un nom et un age, sinon la fonction ne fonctionne pas
# Le nom des paramètres n'a pas d'importance à part la clareté du code
def nom_de_la_fonction(nom, age):
    print("Bonjour " + nom + ", tu as " + str(age) + "ans")


nom_de_la_fonction("Maxence", 28)


# RETURN permet à la fonction de donner directement une information en retour à utiliser dans le code
# Ici, la fonction return 8
def return_cest_pratique(num):
    return num + num


print(return_cest_pratique(4))
# IMPORTANT : Le code écrit après return dans une fonction n'est pas pris en commpte
# return fini la fonction et en sort