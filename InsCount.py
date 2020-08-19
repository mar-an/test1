#class which count his own use - counter increment when create instance that class
class InstanceCounter(object):
    count =0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count