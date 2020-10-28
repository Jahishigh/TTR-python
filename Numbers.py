# Un nombre s'écrit sans ""
print(2)
# On peut utiliser des nombres négatif ou décimal :
print(-2)   # Ceci est un int
print(2.35)  # Ceci est un float
# Faire des opérations basique :
print(1 + 1)
print(1 - 1)
print(2 * 3)
print(4 / 2)
# Utiliser des parenthèses pour l'ordre d'opération
print(3 * (4 + 5))
# Modulus : donne le reste (donc 1 ici)
print(10 % 3)
# Convertir un nombre en string :
# Si on veut print un nombre avec une string, il faut changer le nombre en string sinon tout explose
num_to_string = 5
print(str(num_to_string) + " est une string maintenant")
# Récuperer la valeur absolue
print(abs(num_to_string))
# Récuper la puissance d'un nombre (2 paramètrs, le nombre et la puissance voulue (ici 4^2 = 16):
print(pow(4, 2))
# Return le nombre le plus grand (min fait l'inverse) ici renvoie 6
print(max(4, 6))
# Arrondir un nombre (renvoie 4 ici) :
print(round(3.7))

# Il y en a bien plus avec le module math