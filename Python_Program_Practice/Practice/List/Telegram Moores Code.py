codes  = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

moores_str = ''
string = 'deface'

for i in string:
    moores_str = moores_str + codes[ord(i)-97]+' '

print(moores_str)