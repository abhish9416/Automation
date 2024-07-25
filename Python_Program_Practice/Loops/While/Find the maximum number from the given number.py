def max(total):
    max = 0
    count = 0
    while count < total:
        num = int(input("Enter the Number : "))
        if num > max :
            max = num
        count = count+1
    print(max)


total = int(input("Enter the Number : "))
max(total)