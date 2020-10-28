# Toujours entourer une string avec ""
string_exemple = "Hello World"
# Pour passer la string en lower case :
string_exemple.lower()
# Pour passer la string en upper case :
string_exemple.upper()
# Check si une string est quelque chose, ici upper case (renvoie True or False)
string_exemple.isupper()
# Combinaison de fonctions, ici passer la string en upper puis check si elle est (renvoie True)
string_exemple.upper().isupper()
# Trouver la longueur d'une string (renvoie 12)
len(string_exemple)
# Voir quel caractère à une position précise (renvoie H)
# Ne pas oublier [] est un tableau et les tableau en python commence par 0
print(string_exemple[0])
# Découper une string fonctionne comme ça : [start:stop:stepover]
# print une string d'un start à un stop
print(string_exemple[0:6])
# print une string en sautant des charactère
print(string_exemple[0:6:2])
# commencer au début jusqu'à x
print(string_exemple[:5])
# commencer de là jusqu'à la fin
print(string_exemple[3:])
# partir de la fin
print(string_exemple[-3])
# afficher à l'envers
print(string_exemple[::-1])
# Trouver la position d'un charactère dans la string avec index (renvoie 0 pour la première position)
# Dans index, il faut préciser un paramètre
string_exemple.index("H")
# Index peut être utiliser avec un mot complet (renvoie 6, la position du premier charactère du mot complet
string_exemple.index("Wor")
# .find fait la même chose
string_exemple.find("Wor")
# Remplacer un charactère par un autre (avec 2 paramètres) :
string_exemple.replace("World", "Planet Earth")
# Pour créer une string avec plusieurs lignes, utiliser ''' '''
multi_line_string = ''' Je suis une string
avec plusieurs
lignes
'''

print(multi_line_string)

# formatted strings
name = 'Johnny'
age = 55
print(f"hi {name} ! You are {age} years old !")
# autre solution qui vient de python2, le .format
print('hi {} you are {} years old'.format(name, age))
# changer l'ordre d'apparition avec cette méthode
print('hi {1} you are {0} years old'.format(name, age))
# crée une variable à l'intérieur d'une string
print('hi {new_name} you are {new_age} years old'.format(new_name='Bob', new_age=100))