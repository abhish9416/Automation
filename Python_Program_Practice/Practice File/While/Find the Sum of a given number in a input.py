def sumnum(total):

    sum = 0
    count = 0
    while count < total:
        num = int(input("Enter the Number : "))
        sum = sum + num
        count = count +1
    return sum


total = int(input("Enter the total number : "))
print(sumnum(total))