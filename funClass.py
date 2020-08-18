class function:
    
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
      