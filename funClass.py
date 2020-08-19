import random
class function(object):

    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.newList = []
      

    def kwadrat(self):
        for i in self.x:
            for j in self.y:
                if j == i:
                    self.newList.append(j)
                    print(j)
#               #else:
#               #    print("brak powiązania dla" +str(j))
                
    def showme(self): 
        for (i, item) in enumerate(self.newList, start=1):
            print(i, item)

    def dothis(self):
        self.randomVal = random.randint(1,25)

#function try change val to int, if can't change except work with end func

    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def increment(self):
        self.val = self.val + 1
        return self.val



