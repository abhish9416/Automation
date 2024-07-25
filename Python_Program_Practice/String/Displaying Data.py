item_name = input("Enter the Item Name : ")
item_price =input("Enter the Price of the Item : ")

total_length = len(item_name) + len(item_price)
print(total_length)

dots = '.' * (25 - total_length)
total = item_name+dots+item_price
print(len(total))
print(total)