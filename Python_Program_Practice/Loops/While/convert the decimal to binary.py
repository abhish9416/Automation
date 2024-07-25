def decimaltobinary(num):
    binary = ''
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    secondbinary = binary
    print(type(secondbinary))
    if secondbinary == binary[::-1]:
        print("Binary Number is Palindrome")
    else:
        print("False")
    return binary

num = int(input("Enter the Number : "))
print(decimaltobinary(num))
