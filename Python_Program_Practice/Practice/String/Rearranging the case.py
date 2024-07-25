s1 = 'vvhveuAHFNijd'

lower = ''
upper = ''

for x in s1:
    if x.islower():
        lower = lower+x
    else:
        upper = upper+x

print(lower+upper)

