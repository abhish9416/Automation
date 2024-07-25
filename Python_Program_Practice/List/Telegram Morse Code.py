codes  = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

moores_str = ''
text = 'deface'

for i in text:
     moores_str = moores_str + codes[ord(i)-97]+ ' '
print(moores_str)