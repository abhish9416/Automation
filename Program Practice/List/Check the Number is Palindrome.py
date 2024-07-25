#Check the Given number is Palindrome or not with converting to string

def palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")


num = int(input("Enter the Number: "))

palindrome(num)


#Check if the Number is Palindrome Without converting to string

def palindrome(num):
    while num > 0:
        remainder = num % 10
