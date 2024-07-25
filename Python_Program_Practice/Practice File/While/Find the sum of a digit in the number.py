def sumdigit(num):
    sum = 0
    count = 0
    while num > 0:
        remainder = num % 10
        sum = sum + remainder
        num = num // 10
        count += 1
    return sum

num = int(input("Enter the Number : "))
print(sumdigit(num))