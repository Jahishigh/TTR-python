# Pour lire un fichier, on l'ouvre, on donne le nom du fichier dans une string
# Puis on choisie un mode de lecture :
# r pour seulement lire, w pour modifier le fichier, a pour ajouter quelque chose à la fin du fichier
# r+ permet de lire et écrire
# IMPORTANT : Penser à toujours fermer le fichier
# ton_fichier.readable renvoie un boolean pour vérifier si ton fichier est bien lisible
# ton_fichier.read affiche le contenu de ton fichier
# ton_fichier.readline lis la première ligne de ton fichier, puis déplace le curseur à la ligne suivante dans le fichier
# Du coup si tu refais un .readline, tu lis la ligne suivante, donc la deuxième
# ton_fichier.readlines mets toutes les lignes de ton fichier dans un tableau
# Donc en second paramètre tu peux indiquer la position dans le tableau que tu veux afficher (ici la ligne 1)
# Avec une boucle for, tu peux donc afficher toutes les lignes : for ligne in ton_fichier.readlines()
try:
    ton_fichier = open("nom_de_ton_fichier", "r")
    if ton_fichier.readable() is True:
        print(ton_fichier.read)
        print(ton_fichier.readline())
        print(ton_fichier.readlines()[1])
    ton_fichier.close()
except FileNotFoundError:
    print("Evidemment, le fichier n'existe pas hein")