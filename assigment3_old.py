"""
    Usages:
    ./assignment_3.py                           (reads out the entire config dict)
    ./assignment_3.py thiskey thisvalue         (sets 'thiskey' and 'thisvalue' in the dict)
"""
import os
import sys
class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename

        if os.path.isfile(self._filename):
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, val = line.split('=', 1)
                    # w klasie nadrzednej dict jest tworzona instancja naszego słownika - przez przeczytanie wszystkich linii pliku i dodanie do słownika
                    dict.__setitem__(self, key, val)


    #funkcja klasy nadrzednej dict wywoływana przez dodanie elementu do słownika: cd['klucz3']='wartosc3'
    def __setitem__(self, key,value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w+') as fh:
            # items() iteruj po słowniku pomijając istniejace juz pary key->value
            for key, val in self.items():
                print(key, val)
                fh.write('{0}={1}\n'.format(key, val))





cd = ConfigDict('config_file.txt')
cd['klucz3']='wartosc3'

print(cd)
