l1 = elements = [("id1", "p1", "p2", "p3"),("id2", "p1", "p4", "p5"),("id3", "p6", "p7", "p8"), ("id4", "p6", "p9", "p10")]
duplicate = set()
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        prop_i = set(l1[i][1:])
        prop_j = set(l1[j][1:])

        if prop_i & prop_j:
            duplicate.add((l1[i][0],l1[i][0]))
print(duplicate)
