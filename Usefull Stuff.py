

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# in
use_array = ['a', 'b', 'c', 'd']
print('x' in use_array)  # Renvoie False
print('i' in 'hi my name is Ian')  # Renvoie True

# range
print(list(range(1, 100)))
print(list(range(101)))

# join
new_phrase = ' '.join(['hi', 'my', 'name', 'is', 'jojo'])  # va ajouter un espace après chaque item

# type() donne le type de l'élément donné, ici l'exemple renvoie str
print(type("Hello"))

# fonction pour passer une string dans un array
def convert_to_array(string):
    array = []
    array[:0] = string
    return array

def convert_to_string(array):
    return ', '.join(array)

# None est utile pour montrer que quelque chose n'existe pas
player_weapon = None

# Truthy and Falsy
# Toute les value sont considéré comme True sauf les valeur vide comme None, 0, les listes, string, dict qui sont vide
print(bool('123'))  # renvoie True

# is check si c'est au même endroit dans la mémoire

# déclarer plusieurs variables d'un coup
a, b, c = 1, 2, 3
print(a, b, c)