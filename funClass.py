class function:
    def __init__(self, x, y):
        self.x=[]
        self.y=[]

    def kwadrat(self):
        for i in self.x:
            for j in self.y:
                if j == i:
                    print(j)
                else:
                    print("brak powiązania dla" +str(j))