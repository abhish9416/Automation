def max_int(integer):
    max = 0

    while integer > 0:
        remainder = integer % 10
        if remainder > max:
            max = remainder
        integer = integer // 10
    return max



integer = int(input("Enter the Number: "))
print(max_int(integer))
