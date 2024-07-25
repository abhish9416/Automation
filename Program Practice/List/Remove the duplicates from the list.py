#Remove the Duplicates from the list

def duplicates(lists):
    l2 = []
    for i in lists:
        if i not in l2:
            l2.append(i)
    print(l2)

lists = [1,2,3,3,5,6,6]
duplicates(lists)
