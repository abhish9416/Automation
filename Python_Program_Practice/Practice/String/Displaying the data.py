s1 = input("Enter the Product name: ")
s2 = input("Enter the Product price: ")

total_len = len(s1)+len(s2)

dot = '.'*(25-total_len)
str2 = s1+dot+s2
print(str2)
print(len(str2))