class function:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def kwadrat(self):
        for i in self.x:
            for j in self.y:
                if j == i:
                    print(j)
#               #else:
#               #    print("brak powiązania dla" +str(j))
                
    def showme(self): 
        print("jestem w showme")