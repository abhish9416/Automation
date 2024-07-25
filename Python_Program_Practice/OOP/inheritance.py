class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth
class Cuboid(Rectangle):
    def __init__(self, h, l, b):
        super().__init__(l, b)
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.height


r1 = Rectangle(10,5)

print(r1.area())
print(r1.perimeter())

c1 = Cuboid(10,5,10)
print(c1.volume())