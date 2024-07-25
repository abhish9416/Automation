def returnelement():
    l = [1,2,3,4,6,7,8]

    try:
        index = int(input("Enter the Number : "))
        print(l[index])
    except (IndexError,ValueError,ZeroDivisionError) as ind:
        print(ind)
    except:
        print("Some Error")

    print("Terminated")


returnelement()



