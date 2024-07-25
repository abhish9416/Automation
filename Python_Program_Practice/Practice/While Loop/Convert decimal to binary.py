def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    print(binary)


decimal = int(input("Enter the Number: "))
decimal_to_binary(decimal)