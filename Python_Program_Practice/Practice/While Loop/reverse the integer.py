def reverse_integer(integer):
    reverse = 0
    while integer > 0:
        remainder = integer % 10
        reverse = reverse * 10 + remainder
        integer = integer // 10
    print(reverse)


integer = int(input("Enter the Number: "))
reverse_integer(integer)