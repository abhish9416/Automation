def overlapping(l1,l2):
    l3 = []
    for i in l1:
        if i in l2:
            l3.append(i)
    print(l3)

l1 = [10,12,15,17,16]
l2 = [16,18,12,9,11]
overlapping(l1,l2)