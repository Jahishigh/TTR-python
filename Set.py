# Collection d'item unique
my_set = {1, 2, 3, 4, 5}  # return 1,2,3,4,5 car c'est item unique, donc le deuxième 5 n'est pas affiché
your_set = {4, 5, 6, 7, 8, 9, 10}
# Pour ajouter dans un set
my_set.add(2)  # il sera dans le set, mais pas affiché car un 2 existe déjà
# Pour changer une liste en set pour enlever les duplicate d'une liste
my_list = [1, 2, 3, 4, 5, 5]
set(my_list)  # return 1,2,3,4,5
# Pour voir si quelque chose exite dans le set
print(1 in my_set)  # return True
# .difference compare 2 set
my_set.difference(your_set)  # return 1,2,3 -> Il regarde your_set et voit qu'il manque 1,2,3 par rapport à lui
# .discard enleve un élement d'un set
my_set.discard(5)  # enleve un élément dans le set -> ici return 1,2,3,4 si on print my_set
# .difference_update enleve les différences entre 2 set
my_set.difference_update(your_set)  # return 1,2,3 et à supprimé 4 et 5 de my_set
# .intersection donne les intersections entre 2 set
my_set.intersection(your_set)  # return 4,5
print(my_set & your_set)  # renvoi la même chose
# .isdisjoint vérifie si les 2 set n'ont rien en commun
my_set.isdisjoint(your_set)  # renvoi False car 4,5 est en commun dans les deux
# .union unie 2 set et enlève les duplicate et crée un nouveau set
my_set.union(your_set)  # renvoi 1,2,3,4,5,6,7,8,9,10
print(my_set | your_set)  # renvoi la même chose