"""
dodanie do pliku konf wartości typu email=marian@gmail.com
obsługa wyjątków, błedna scieżka, brak uprawnien do zapisu, nieistniejący klucz w słowniku
    Usages:
    ./assignment_3.py                           (reads out the entire config dict)
    ./assignment_3.py thiskey thisvalue         (sets 'thiskey' and 'thisvalue' in the dict)
"""
import os
import pickle

class ConfigKeyError(Exception):                                                       # klasa obsługi wyjątku braku klucza, wywołanie nieistaniejącego klucza np cd['klucz4']
    def __init__(self, this, key):                                                     # this to przekazany obiekt konfliktu typu dict, self to obiekt konfliktu self, key to nieistniejący klucz
        self.key = key
        self.keys = this.keys()                                                        # keys - klucze dostepne w konflikcie dict (chcemy pokazac użytkownikowi które klucze są dostępne jesli wywołał klucz nieistniejący)
    def __str__(self):                                                                 # funkcja __str__ działa kiedy nastąpi wyjątek
        return 'key "{0}" not found. Avialable keys: ({1})'.format(self.key, ', '.join(self.keys))

class ConfigDict(dict):

    config_directory = "C:\\Users\\dudam\\PycharmProjects\\test1\\config"

    def __init__(self, picklename):
        self._filename = os.path.join(self.config_directory, picklename + '.pickle')

        if not os.path.isfile(self._filename):
            with open(self._filename, 'wb') as fh:
                pickle.dump("a", fh)
        with open(self._filename, 'rb') as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

                                                                                            # w klasie nadrzednej dict jest tworzona instancja naszego słownika - przez przeczytanie wszystkich linii pliku i dodanie do słownika

    def __getitem__(self, key):                                                         # motoda dp spr czy wywoływany klucz a dict intnieje w razie takiego wywołania cd['klucz4']
        if not key in self:                                                             # spr czy klucz wywoływany istnisje
            raise ConfigKeyError(self, key)                                             # jesli nie istnieje uruchom instancję klasy obsługi wyjątku: ConfigKeyError
        return dict.__getitem__(self, key)                                              # jesli istnieje dokoncz normalnie procedurę __getitem__


    def __setitem__(self, key, value):                                                   #funkcja klasy nadrzednej dict wywoływana przez dodanie elementu do słownika: cd['klucz3']='wartosc3'
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            pickle.dump(self, fh)



cd = ConfigDict('config_file')
cd['klucz3']='wartosc3'

print(cd)
