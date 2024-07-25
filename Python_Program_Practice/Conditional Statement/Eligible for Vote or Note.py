def eligible(age):
    if age >= 18:
        print("Candidate is Eligible to Cast Vote")
    else:
        print("Candidate is not Eligible to Cast Vote")


age = int(input("Enter the age : "))
eligible(age)