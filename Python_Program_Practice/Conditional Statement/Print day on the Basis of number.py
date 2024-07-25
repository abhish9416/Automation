def daynumber(userchoice):
    if userchoice == '1':
        print("Sunday")
    elif userchoice == '2':
        print("Monday")
    elif userchoice == '3':
        print("Tuesday")
    elif userchoice == '4':
        print("Wednesday")
    elif userchoice == '5':
        print("Thursday")
    elif userchoice == '6':
        print("Friday")
    elif userchoice == '7':
        print("Saturday")

userchoice = input("Enter the Day Number : ")
daynumber(userchoice)