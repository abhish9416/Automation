import math

def circle(r):
    area = math.pi*r*r
    return area

r = int(input("Enter the Radius of the circle : "))
print(circle(r))