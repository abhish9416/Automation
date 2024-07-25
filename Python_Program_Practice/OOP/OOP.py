class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth

r1 = Rectangle(10,5)

print(r1.area())
print(r1.perimeter())
