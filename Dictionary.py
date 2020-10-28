# Un dictionary permet d'associer une key à une valeur
# A utiliser quand on a beaucoup d'information que ne doivent pas forcément être dans l'ordre comme dans une liste
# Une key doit être immuable, donc par exemple une string, un int ou un bool
# Mais on utilise princpalement des string pour être descriptif
mon_dico = {
    "Jan": "Janvier",
    "Feb": "Fevrier",
    "Mar": "Mars",
    "Num": 5,
    10: "Dix",
    'tab': [1, 2, 3]
}
print(mon_dico["Feb"])
print(mon_dico["Num"])
# On peut aussi utiliser une fonction pour appeler une value du dico :
print(mon_dico.get("Jan"))
# pour voir si un dico a une key
print(mon_dico.get("Avr"))
# Si la value n'est pas dans le dico, on peut fournir une valeur de base en parametre pour prévenir de l'erreur
print(mon_dico.get("Avr", "C'est pas dans le dico"))
# pour copier un dictionary
mon_dico2 = mon_dico.copy()
# pour vider un dictionary
mon_dico.clear()

# autre moyen de faire un dictionary
user = dict(name='john')

# pour loop dans un dict :
# affiche les key + value dans un tuple
for item in mon_dico.items():
    print(item)
# affiche les key + value sans tuple car on unpack dans la loop
for key, value in mon_dico.items():
    print(key, value)
# affiche les values
for item in mon_dico.values():
    print(item)
# affiche les keys
for item in mon_dico.keys():
    print(item)