def countof_element(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
            count = l1.count(i)
            l2.append(count)
    print(l2)


l1 = ['a', 'b', 'c', 'd', 'a', 'e', 'a']
countof_element(l1)
