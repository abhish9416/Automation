def multable(num):
    count = 1
    while count <= 10:
        print(num,"x",count,"=",num*count)
        count = count +1

num = int(input("Enter the Number : "))
multable(num)