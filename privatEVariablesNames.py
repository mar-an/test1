class GetSet(object):

    instance_count = 0
# zmienna public
    regular_lower_case
# zmienna private
    _single_leading_underscore
# zmienna prywatna nie do użytku w klasie podrzędnej
    __double_leading_underscore
# zmianna magiczna
    __magic_var__

# zmienna nie do użycia w klasie podrzędnej __
    __mangled_name = 'no privacy!'

# zmienna privat _ (_ to tylko umowne oznaczenie, do zmiennej jest dostęp jak w linii 30)
    def __init__(self, value):
        self._attrval = value
        GetSet.instance_count += 1

    @property
    def var(self):
        print("getting the 'var' attribute")
        return self._attrval

    @var.setter
    def var(self, value):
        print("setting the 'var' attribute")
        self._attrval = value

    @var.deleter
    def var(self):
        print("deleting the 'var' attribute")
        self._attrval = None

cc = GetSet(5)
cc.var = 10
print(cc._attrval)

#dostęp do zmiennej __mangled_name
print(cc._GetSet__mangled_name)

# brak dostępu do zmiennej __mangled_name (bezposrednio nie działa)
# nie ma jednoznacznego okreslenia czy atrybutu zmiennej by zabronic do niej dostepu wszystko jest kwestią konwencji, umowy
# print(cc.__mangled_name)