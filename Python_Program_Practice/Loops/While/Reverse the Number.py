def reversenumber(num):
    reverse = ''
    while num > 0:
        remainder = num % 10
        reverse = reverse + str(remainder)
        num = num // 10
    return reverse


num = int(input("Enter the Number : "))
print(reversenumber(num))