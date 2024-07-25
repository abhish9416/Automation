def leapyear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year is a leap Year")
        else:
            print("Year is Not a Leap Year")
    elif year % 4 == 0:
        print("Year is Leap Year")
    else:
        print("Year is Not a Leap Year")

year = int(input("Enter the Year : "))
leapyear(year)
