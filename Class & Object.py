# Crée une classe permet de définir autre chose qu'une string ou un boleean mais de représenter un 'objet'
# Lorsqu'on crée une class, un crée une def qui permet de donner des paramètres relié à cet objet
# __init__ sert à recevoir des paramètres et les stocker dans les paramètre donné dans la def
# self.ton_paramètre sert à attribuer à ton objet les paramètres que tu as donné
# Dans l'exemple, en passant un string avec le nom, on le recois dans init puis on l'attribut à l'objet avec self
# IMPORTANT, si on crée la class dans un autre fichier, ce qui est recommandé, penser à l'importer
# Par exemple ici si la class est dans un fichier nommé animals.py : from animals import pet
# Dans le code, on peut appeler la classe en donnant une variable, puis en appelant la class, et donner les paramètres
# Une fois l'objet crée, on peut maintenant facilement accéder à toutes ses informations comme dans le print ci dessous
# On peut aussi def des fonctions que l'on peut appeler avec cet objet, comme ici speak
# A savoir que l'on est pas obligé d'init des paramètre dans la class, on peut juste mettre des fonctions à executer
# Dans une class, on peut aussi avoir un attribut sans le demander en parametre pour l'ajouter plus tard par un autre
# moyens, ici self.is_true n'est pas demandé dans les paramètre de init, mais on pourra l'ajouter plus tard en faisant
# par exemple : self.is_true = False
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_true = True
    def speak(self):
        print("What am i ?")
    def show(self):
        print("Je suis " + self.name + " et j'ai " + str(self.age) + "ans")

p = Pet("Tim", 19)
p.speak()

# Pour faire hériter une class de ce que possède une autre class, ajouter le nom de la class entre parenthèse
# Ici, Cat peut utiliser les paramètre de Pet car il a hésité de sa class, et peut utiliser un fonction exclusive
# qui vient de sa propre class speak("Meow")
class Cat(Pet):
    def speak(self):
        print("Meow")

c = Cat("Nougat", 2)
c.show()
c.speak()

# Si on ne défini rien dans une nouvelle class enfant, on peut mettre pass, ce qui va juste prendre les attribut de sa
# class parente
class Fish(Pet):
    pass

f = Fish("Nemo", 3)
f.show()
f.speak()

# Si on veut rajouter un paramètre à entrer dans init qui n'est pas dans la class parente
# super() appel la class parente, donc ici on appel name et age de Pet et on y ajoute color pour cette class uniquement
class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Bark")

    def show(self):
        print("Je suis " + self.name + ", j'ai " + str(self.age) + "ans et je suis " + self.color)

d = Dog("Rex", 5, "marron")
d.show()
d.speak()

# Attribut de class
# Ici, number_of_people est un attribut de class, était en dehors de l'init, il ne change pas à chaque objet mais est
# attribué à la class entière
# Du coup, à chaque nouvel objet, je peux incrémenter cette attribut, et l'appeler
class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people)

# Les class method sont des fonctions aggissent sur la class entière et non sur un objet
# Ici, pour calculer le nombre de personne, on appel la fonction add_person à l'intérieur de l'init pour incrémenter
# nb_of_ppl puis on print nb_ppl qui return notre attribut de class
class ppl:
    nb_of_ppl = 0
    def __init__(self, name):
        self.name = name
        ppl.add_person()
    @classmethod
    def nb_ppl(cls):
        return cls.nb_of_ppl
    @classmethod
    def add_person(cls):
        cls.nb_of_ppl += 1

Pa = ppl("Jean")
Pb = ppl("Marc")
print(ppl.nb_ppl())

# Les static method sont des fonctions dans des class qui ne prennent aucun attribut, ni de self ni de cls
# Elle sont dans la class mais n'ont accès à rien et peuvent juste être appelé sans rien changer à la class et ses init
# On les utilise souvent pour ranger des fonctions qui ont une utilité similaire pour les appeler plus facilement
class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))
Math.pr()