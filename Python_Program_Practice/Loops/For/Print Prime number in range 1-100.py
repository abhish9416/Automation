def prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(i)
    else:
        print("No Prime Numbers found")

num = int(input("Enter the Number : "))
prime(num)

