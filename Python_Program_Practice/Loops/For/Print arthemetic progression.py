def apseries(start,end,diff):
    for i in range(start, end * diff + start,diff):
        print(i)


start = int(input("Enter the Number : "))
end = int(input("Enter the End Number : "))
diff = int(input("Enter the Difference Number :"))
apseries(start,end,diff)