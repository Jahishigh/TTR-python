# Ceci permet d'attraper une erreur pour ne pas qu'elle s'affiche et qu'elle bloque notre code
# A la place, on peut s'en occuper et lui donner quelque chose à faire si une erreur arrive
# Dans l'exemple, si on entre autre chose qu'un nombre entier, au lieu de crash le code, on va renvoyer une string
# Pour ce code, on pourrait mettre tout ça dans un while pour donner une nouvelle chance d'entrer un nombre entier
# IMPORTANT : dans le except, il faut préciser le type d'erreur qu'on veut attraper
# Si on ne met rien, il va attraper toutes les erreurs, mais mettre toujours le même message
# Pour afficher le message d'erreur, ajouter as err (qu'importe le nom, pas forcément err) et print err
try:
    nombre = int(input("Entrer un nombre entier"))
    print(nombre)
except ValueError as err:
    print("C'est pas un nombre entier ça")
    print(err)