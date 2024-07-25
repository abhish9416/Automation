# def decimal_to_binary(decimal):
#     decimal = bin(decimal)[2:]
#     print(decimal)
#
# n=12
# for i in range(1, n-1):
#     binary = decimal_to_binary(i)
#     print(binary)

def binary_to_decimal(n):
    for decimal in range(1,n-1):
        binary = bin(decimal)[2::]
        print({decimal},'in binary Format',{binary})
        # if binary == str(binary)[::-1]:
        #     print({decimal},'is palindrome in binary representation',{binary})



n = int(input("Enter the Number"))
binary_to_decimal(n)

