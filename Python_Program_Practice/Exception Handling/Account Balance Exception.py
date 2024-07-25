class Accountbalanceexception(Exception):
    pass

balance = 10000

def amount(amt):
    global balance
    if balance - amt < 5000:
        raise Accountbalanceexception("Please Lower the amount since minimum balance need to be maintained is 5000")
    else:
        balance = balance - amt
        print('Remaining balance',balance)


amt = int(input("Enter the Amount : "))

try:
    amount(amt)
except Accountbalanceexception as e:
    print(e)