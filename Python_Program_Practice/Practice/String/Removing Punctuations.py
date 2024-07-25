punctutaion = '''!@$#%^&*"':;{}[]()-_',./'''

s1 = '[(/my,email,-@gmail.com'

s2 = ''

for x in s1:
    if x not in punctutaion:
        s2 = s2+x
print(s2)