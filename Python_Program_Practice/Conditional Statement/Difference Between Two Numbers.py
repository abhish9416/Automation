def difference(num1,num2):
    if num1 - num2 > 0:
        print(num1-num2)
    else:
        print(num2 - num1)

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

difference(num1,num2)