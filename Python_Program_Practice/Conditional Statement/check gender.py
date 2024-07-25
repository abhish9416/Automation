def checkgender(gender):
    if gender == 'm' or gender == 'M':
        print("You are a Male")
    else:
        print("You are female")

gender = input("Enter your gender : ")
checkgender(gender)