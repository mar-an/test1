#class give limited output only (per instance)
class MaxSizeList(object):
    def __init__(self, val):
        self.val = val
        self.newList = []

    def push(self, val1):
        if(len(self.newList)  < self.val):
            self.newList.append(val1)
        elif len(self.newList)   > self.val:
            self.newList.pop(0)

    def get_list(self):
        return self.newList