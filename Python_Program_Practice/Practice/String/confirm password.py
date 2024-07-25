s1 = input("Enter the Password: ")
s2 = input("Confirm the Password: ")

if s1 == s2:
    print("password matches")
else:
    if s1.casefold() == s2.casefold():
        print("Please Check the cases")
    else:
        print("Password Does not matches")