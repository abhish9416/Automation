def sum_of_digit(integer):
    sum = 0
    while integer > 0:
        remainder = integer % 10
        sum = sum + remainder
        integer = integer // 10

    return sum

integer = int(input("Enter the Number"))
print(sum_of_digit(integer))