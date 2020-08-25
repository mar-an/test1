"""
dodanie do pliku konf wartości typu email=marian@gmail.com
obsługa wyjątków, błedna scieżka, brak uprawnien do zapisu, nieistniejący klucz w słowniku
    Usages:
    ./assignment_3.py                           (reads out the entire config dict)
    ./assignment_3.py thiskey thisvalue         (sets 'thiskey' and 'thisvalue' in the dict)
"""
import os

class ConfigKeyError(Exception):                                                       # klasa obsługi wyjątku braku klucza, wywołanie nieistaniejącego klucza np cd['klucz4']
    def __init__(self, this, key):                                                     # this to przekazany obiekt konfliktu typu dict, self to obiekt konfliktu self, key to nieistniejący klucz
        self.key = key
        self.keys = this.keys()                                                        # keys - klucze dostepne w konflikcie dict (chcemy pokazac użytkownikowi które klucze są dostępne jesli wywołał klucz nieistniejący)
    def __str__(self):                                                                 # funkcja __str__ działa kiedy nastąpi wyjątek
        return 'key "{0}" not found. Avialable keys: ({1})'.format(self.key, ', '.join(self.keys))

class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if not os.path.isfile(self._filename):                                          # jesli nie ma pliku probuj go otworzyć
            try:
                open(self._filename, 'w').close()
            except IOError:                                                             # jesli nie ma dostepu do pliku (nieistniejąca sciezka, brak uprawnien) kieruj do obsługi wyjatków
                raise IOError('arg to config must be valid pathname')
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, val = line.split('=', 1)
                    dict.__setitem__(self, key, val)                                    # w klasie nadrzednej dict jest tworzona instancja naszego słownika - przez przeczytanie wszystkich linii pliku i dodanie do słownika

    def __getitem__(self, key):                                                         # motoda dp spr czy wywoływany klucz a dict intnieje w razie takiego wywołania cd['klucz4']
        if not key in self:                                                             # spr czy klucz wywoływany istnisje
            raise ConfigKeyError(self, key)                                             # jesli nie istnieje uruchom instancję klasy obsługi wyjątku: ConfigKeyError
        return dict.__getitem__(self, key)                                              # jesli istnieje dokoncz normalnie procedurę __getitem__


    def __setitem__(self, key,value):                                                   #funkcja klasy nadrzednej dict wywoływana przez dodanie elementu do słownika: cd['klucz3']='wartosc3'
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w+') as fh:
            for key, val in self.items():                                               # items() iteruj po słowniku pomijając istniejace juz pary key->value
                fh.write('{0}={1}\n'.format(key, val))





cd = ConfigDict('config_file.txt')
cd['klucz5']='wartosc5'

print(cd)
