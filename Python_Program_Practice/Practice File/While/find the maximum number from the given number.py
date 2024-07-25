def maxnumber(num):
    max = 0
    count = 0
    while count < num:
        remainder = num % 10
        if remainder > max:
            max = remainder
        num = num //10
        count = count +1
    return max

num = int(input("Enter the Number : "))
print(maxnumber(num))
