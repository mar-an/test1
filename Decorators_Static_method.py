
class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        #self.val = val                     #dla @classmethod
        self.val = self.filterint(val)     #dla @staticmethod
        InstanceCounter.count += 1

    def get_val(self):
        return self.val

# metoda klasy nie ma odniesienia do instancji, ale mozna ja z instancji wywolac
    @classmethod
    def get_count(cls):
        return cls.count

# metoda statyczna, nalezy do klasy ale nie dziala z instancja - w tym wypadku wywolywana z konstruktora sprawdza czy argument instancji jest INT
    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(6.3)
b = InstanceCounter(13)
c = InstanceCounter(17)

#dla @classmethod
#for obj in (a, b, c):
#    print("val of obj: %s" % (obj.get_val()))
#    print("count: %s" % (obj.get_count()))

#dla @staticmethod
print (a.val)
print (b.val)
print (c.val)