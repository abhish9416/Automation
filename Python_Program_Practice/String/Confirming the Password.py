pass1 = input("Enter the Password")
pass2 = input("Enter the Passeord Again")

if pass1 == pass2:
    print("password match")
else:
    if pass1.casefold() == pass2.casefold():
        print("Please check the password cases again")
    else:
        print("No password is not matching")