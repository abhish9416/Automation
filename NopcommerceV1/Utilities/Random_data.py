from faker import Faker

fake = Faker()

def first_name_gen():
    return fake.first_name()

def last_name_gen():
    return fake.last_name()

def email_gen():
    return fake.email()