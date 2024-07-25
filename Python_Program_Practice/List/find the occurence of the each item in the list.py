l1 = ['a','b','c','d','a','e','a']

result = []

for i in l1:
    if i not in result:
        result.append(i)
        count = l1.count(i)
        result.append(count)
        
print(result)