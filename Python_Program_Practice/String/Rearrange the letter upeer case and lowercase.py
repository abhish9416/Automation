s1 = 'bchAuIhES'

lower = ''
upper = ''

for x in s1:
    if x.islower():
        lower += x
    else:
        upper += x
print(lower+upper)