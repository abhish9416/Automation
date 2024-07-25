def palindrome(num):
    reverse = 0
    number = num
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10
    # return reverse
    if number == reverse:
        print("Number is Palindrome")
    else:
        print("Number is Not a Palindrome")
    print(reverse)

num = int(input("Enter the number : "))
palindrome(num)