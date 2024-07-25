def binary(num):
    binary = ''
    while num > 0:
        ramainder = num % 2
        binary = str(ramainder) + binary
        num = num // 2
    return binary

num = int(input("Enter the Number : "))
print(binary(num))