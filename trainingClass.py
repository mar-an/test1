class MyNum(object):

# init which do preperation work like check if file is correct format like CSV or XML
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            print ("don't use NOT string value like " +value)
            exit(1)
        self.val = value

    def increment(self):
        self.val = self.val + 1