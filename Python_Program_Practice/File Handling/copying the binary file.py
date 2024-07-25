file = open('640px-Python.svg.png','rb')

data = file.read()

file2 = open('python2.png','wb')

file2.write(data)

file.close()
file2.close()