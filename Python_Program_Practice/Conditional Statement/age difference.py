def agedifference(ajay,binod,suraj):
    if ajay > binod and ajay > suraj:
        print("Ajay is elder")
    elif binod > suraj:
        print("Binod is Elder")
    else:
        print("Suraj is elder")

ajay = float(input("Enter the Ajay Age : "))
binod = float(input("Enter the binod Age : "))
suraj = float(input("Enter the suraj Age : "))

agedifference(ajay,binod,suraj)