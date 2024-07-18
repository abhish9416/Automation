from faker import Faker

fake = Faker()

def emailgenerator():
    email = fake.email()
    return email

def firstnamegenerator():
    first_name = fake.first_name()
    return first_name

def lastnamegenerator():
    last_name = fake.last_name()
    return last_name

def phonegeneratore():
    phone_num = fake.basic_phone_number()
    return phone_num





