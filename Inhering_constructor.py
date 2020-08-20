import random
class Animal(object):

    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):

        # super funkcja wbudowana wiaze nasza klasae z klasa (Animal) by uzywac jej metod, w tym wypadku chcemy użyc konstruktora klasy Dog
        super(Dog, self).__init__(name)
        # dalsza czesc konstruktora ktory jest niezalezny od klasy parent
        self.breed = random.choice(['1', '2', '3'])

d = Dog ('dogname')


print (d.name)
print (d.breed)