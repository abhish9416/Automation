def multiplicationtable(num):
    count = 1
    while count <=10:
        multiplication = num * count
        print(num,"x",count,"=",multiplication)
        count +=1


num = int(input("Enter the Number : "))
multiplicationtable(num)
