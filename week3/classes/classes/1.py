class Person:
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
res = Person()
res.getString()
res.printString()