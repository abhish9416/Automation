def prime(num):
    for n in range(1,num+1):
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count +=1
        if count == 2:
            print(n)


num = int(input("Enter the Number : "))
prime(num)