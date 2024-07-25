def sum(num):
    sum = 0
    while num > 0:
        remainder = num % 10
        sum = sum + remainder
        num = num // 10
    return sum

num = int(input("Enter the Number : "))
print(sum(num))