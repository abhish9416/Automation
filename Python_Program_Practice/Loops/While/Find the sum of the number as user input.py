def sumdigit(total_number):
    sum = 0
    count = 0
    while count < total_number:
        num = int(input("Enter the Number : "))
        sum = sum + num
        count +=1
    print(sum)


total_number = int(input("Enter the total Number : "))
sumdigit(total_number)