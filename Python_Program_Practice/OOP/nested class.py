class Customer:
    def __init__(self,id,name,bdno,bstreet,bpincode,bcity,bcountry,sdno,sstreet,spincode,scity,scountry):
        self.id = id
        self.name = name
        self.baddr = self.Address(bdno,bstreet,bpincode,bcity,bcountry)
        self.saddr = self.Address(sdno,sstreet,spincode,scity,scountry)

    class Address:
        def __init__(self,dno,street,pincode,city,country):
            self.dno = dno
            self.street = street
            self.pincode = pincode
            self.city = city
            self.country = country

        def display(self):
            print(self.dno)
            print(self.street)
            print(self.pincode)
            print(self.city)
            print(self.country)


c1 = Customer(10,'Abhishek',14,'Hitec',94538,'Hyderabad','India',15,'Hitec',94538,'Hyderabad','India')
c1.baddr.display()
print('-------------')
c1.saddr.display()