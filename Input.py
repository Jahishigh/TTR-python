# Pour récupérer ce que l'utilisateur écrit dans une variable
# Le paramètre de l'input est le texte pour l'utilisateur
input_du_user = input("Entrer quelque chose: ")
# Une fois qu'on a récupéré l'input dans une variable, on peut le print ou s'en servir pour autre chose
print("Vous avez écrit " + input_du_user)
# Si on veut que l'user entre un chiffre, on doit le convertir car input return un string de base
# Pour un nombre entier utiliser int, pour un décimal (comprend aussi les entiers) utiliser float
num1 = input("Entrer un nombre entier: ")
num2 = input("Entrer un nombre décimal ou entier: ")
print(int(num1) + float(num2))