class functions:
    def __init__(self, x, y):
        x=[]
        y=[]

    def kwadrat(self, x, y):
        functions.x = x
        functions.y = y
        for i in x:
            for j in y:
                if j == i:
                    print(j)
                else:
                    print("brak powiązania dla" +str(j))