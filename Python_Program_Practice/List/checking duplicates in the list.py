l1 = [1,4,5,4,7,6,7,9]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)