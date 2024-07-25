from faker import Faker

fake = Faker()

random_name = fake.name()
randon_email = fake.email()
random_phone = fake.phone_number()


print('Name : ',random_name)
print('email :',randon_email)
print('phone :',random_phone)