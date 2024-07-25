number_of_hours =[int(x) for x in input("Enter the Working Hours of the week, separated by spaces: ").split()]
wages = int(input("What is the hourly wages"))
total_working = sum(number_of_hours)
print("Total Payable amount is :",wages*total_working)
