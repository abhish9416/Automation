def number_of_digit(integer):
    count = 0
    while integer > 0:
        remainder = integer % 10
        integer = integer // 10
        count += 1
    return count


integer = int(input("Enter the Number: "))
print(number_of_digit(integer))
