class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, lenght):
        self.length = lenght
    def area(self):
        return self.length*self.length
n = int(input())
aSquare = Square(n)
print (aSquare.area())

        