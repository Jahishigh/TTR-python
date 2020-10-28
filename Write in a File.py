# Pour écrire dans le fichier, choisir le bon mode déjà, ici par exemple a pour ajouter à la fin
# ton.fichier.write permet d'écrire dans le fichier (selon le mode choisi)
# Attention, si on relance le code ci dessous, le string ne passera pas à la ligne suivante, donc ajouter un \n au début
# Bien penser à mettre la nature de ton fichier (.txt, .html etc..)
try:
    ton_fichier = open("nom_de_ton_fichier", "a")
    ton_fichier.write("String qui s'ajoute à la fin du fichier")
    ton_fichier.close()
except FileNotFoundError:
    print("Evidemment, le fichier n'existe pas hein")
except PermissionError:
    print("y'a pleins d'erreurs comme y'a pas de fichier")
# Ici on utilise le mode w, ça va donc supprimer tout ce qui a sur le fichier et ajouter que cette ligne
# Avec le mode w, si le nom de ton fichier n'existe pas, python va créer le fichier pour toi
# Par exemple, open("index.html", "w") ton_fichier.write("<h1>Titre</h1>") Va créer une page html et un titre dedans
# ATTENTION Si tu run le code, il va te créer le fichier
try:
    ton_fichier = open("nom_de_ton_fichier.txt", "w")
    ton_fichier.write("oups j'ai tout supprimé")
    ton_fichier.close()
except FileNotFoundError:
    print("Evidemment, le fichier n'existe pas hein")
except PermissionError:
    print("y'a pleins d'erreurs comme y'a pas de fichier")

# Pour supprimer un fichier, il faut import os
# os.remove("nom_de_ton_fichier.txt")
# os.remove("nom_de_ton_fichier")