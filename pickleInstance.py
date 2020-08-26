import pickle

class MyClass(object):
    def __init__(self, init_val ):
        self.val = init_val
    def increment(self):
        self.val += 1

cc = MyClass(5)
cc.increment()
cc.increment()

with open('datafile', 'wb') as fh:                # zapis stanu instancji klasy w formie binarnej python do pliku (mozna takze zapisac stan do YAML, JSON)
    pickle.dump(cc, fh)

with open('datafile', 'rb') as fh:
    unpicked_cc = pickle.load(fh)

print (unpicked_cc)
print (unpicked_cc.val)
