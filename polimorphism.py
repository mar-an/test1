# different outputs depending on which class the instance belong to
# method of the class Cat and Dog have the same name 'show_affection' but give diferent output (common gate)
class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("{0} goes after the %s!".format% (self.name, thing))

    def show_affection(self):
        print('{0} wags tail'.format(self.name))


class Cat(Animal):

    def swatstring(self):
        print("{0} shreds the string!".format(self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))
