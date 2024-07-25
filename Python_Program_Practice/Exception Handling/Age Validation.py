class Negativeage(Exception):
    pass

def stage(age):
    if age < 0:
        raise Negativeage('Age Should be more than 0')
    elif age >= 0 and age < 13:
        print('Kid')
    elif age >=13 and age < 20:
        print('Teen')
    elif age >=20 and age <= 50:
        print('Young')


age = int(input("Enter the Age : "))

try:
    stage(age)
except Negativeage as e:
    print(e)
