file = open('logger.txt','r+')
str1 = file.read()
print(str1)
file.write(''' Now my work is completed 
i have to go home''')
