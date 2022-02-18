class Rectangle:
    def __init__(self, lenght, width):
        self.length = lenght
        self.width  = width
    def area(self):
        return self.length*self.width
lenght,width=map(int,input().split())
aRectangle = Rectangle(lenght,width)
print(aRectangle.area())