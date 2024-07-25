def trapezium(a, b, h):
    area = 1/2 * (a + b) * h
    return area


a = float(input("Enter the Side A : "))
b = float(input("Enter the Side B : "))
h = float(input("Enter the Height : "))
print(trapezium(a,b,h))