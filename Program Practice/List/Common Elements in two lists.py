# Remove common Elements from the list -
def common(l1, l2):
    l3 = []
    for ele in l1:
        if ele in l2:
            l3.append(ele)
    print(l3)


l1 = [1, 2, 3, 4, 5]
l2 = [5, 2, 4, 7, 8]

common(l1, l2)
