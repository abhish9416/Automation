def table(num,n):
    for i in range(1,n+1):
        print(num,'x',i,'=',i*num)


num = int(input("Enter the number : "))
n = int(input("Enter the Number till you want table : "))
table(num,n)