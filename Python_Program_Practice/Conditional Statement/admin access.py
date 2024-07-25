def adminaccess(name):
    if name == 'john' or name == 'smith':
        print("Person is autorized")
    else:
        print("Person is not authorized")

name = input("Enter Your Name : ")
adminaccess(name)