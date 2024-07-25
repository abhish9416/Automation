l1 = [('id1', 'p1', 'p2', 'p3'), ('id2', 'p1', 'p4', 'p5'),('id3', 'p6', 'p7', 'p8'),('id4', 'p6', 'p9', 'p10')]

l2 = []

for i in range(len(l1)):
    duplicate = []
    for j in range(len(l1[0])):
        if l1[i] == l1[j]:
            duplicate.append(l1[i][j])
    l2.append(duplicate)

print(l2)
