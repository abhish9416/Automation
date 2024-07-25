def discountamount(bill):
    global discount
    if bill <= 1000:
        discount = bill * 10/100
    elif 1000 < bill <= 5000:
        discount = bill * 20/100
    elif 5000 < bill <= 10000:
        discount = bill * 30/100
    elif bill > 10000:
        discount = bill * 50/100
    bill = bill - discount
    print(bill)

bill = int(input("Enter the Bill amount : "))
discountamount(bill)