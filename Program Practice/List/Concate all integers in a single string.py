#Concate the List into one string

def onestring(l1):

    string_list = [str(x) for x in l1]
    adding = "".join(string_list)
    print(adding)

l1 =[1,2,3,4,5,6,7]
onestring(l1)