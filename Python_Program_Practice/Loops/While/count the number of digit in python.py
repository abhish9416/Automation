def counter(num):
    count = 0
    while num > 0:
        num = num //10
        count +=1
    return count


num = int(input("Enter the Number : "))
print(counter(num))
