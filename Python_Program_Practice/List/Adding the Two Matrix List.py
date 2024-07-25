a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]

c = []
for i in range(len(a)):
    s = []
    # print(i)
    # print('-----')
    for j in range(len(a[0])):
        s.append(a[i][j]+b[i][j])
    c.append(s)
print(c)

