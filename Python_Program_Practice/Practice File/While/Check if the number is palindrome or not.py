def palindrome(num):
    reverse = 0
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10
    return reverse


num = int(input("Enter the Number : "))
print(palindrome(num))