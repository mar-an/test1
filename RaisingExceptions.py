# Raising exceptions:

myDict = {'a':1, 'b':2, 'c':3, 'd':4}

# try: blok w którym sprawdzamy czy wystąpił błąd
try:
    print (5/0)
# except: blok w który wykonujemy po błędzie
# zmienna e to instancja klasy wyjątku
except ZeroDivisionError, e:
    print(e.message)
    print(e.args)



