date = input("Enter the date in mm/dd/yyyy Format: ")

splitted = date.split('/')

print(splitted)
print('Day',splitted[0])
print('Month',splitted[1])
print('Year',splitted[2])