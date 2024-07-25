a = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

c = []

for i in range(len(a[0])):
    sum = []
    for j in range(len(a)):
        sum.append(a[j][i])
    c.append(sum)

print(c,end='\n')