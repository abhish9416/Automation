def isbinary(num):
    binary = ''
    if num ==  0:
        return 0
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    return binary

num = int(input("Enter the Number : "))

print(isbinary(num))



