def workeligible(age):
    if age >= 18 and age <= 60:
        print("Eligible for Work")
    else:
        print("Not Eligible for work")


age = int(input("Enter Your age"))
workeligible(age)