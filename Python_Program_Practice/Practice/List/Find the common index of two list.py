l1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']
l2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']

index1 = len(l1)+1
index2 = len(l2)+1

for i in range(len(l1)):
    indx = l2.index(l1[i])

    print(indx)
    if i + indx < index1+index2:

        index1 = i
        index2 = indx
print(l2[index2] ,index1+index2)