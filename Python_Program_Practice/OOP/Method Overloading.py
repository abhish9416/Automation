class Sum:
    def add(self,a,b,c=None):
        s = a+b
        if c == None:
            return s
        else:
            return s+c

a = Sum()

print(a.add(10,5,3))
print(a.add('Hello','World'))