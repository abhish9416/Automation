def displacement(v,u,a):
    dis = (v**2 - u**2)/(2*a)
    return dis


v = float(input("Enter the Final Velocity : "))
u = float(input("Enter the initial Velocity : "))
a = float(input("Enter the acceleration : "))

print(displacement(v,u,a))