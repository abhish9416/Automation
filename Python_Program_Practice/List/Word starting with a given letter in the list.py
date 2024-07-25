l1 = ['green','blue','yellow','pink']

letter = input("Enter the letter")

for i in l1:
    if i.startswith(letter):
        print(i)