# def int_to_roman(num):
    # Dictionary of Roman numerals
roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    # List of keys in descending order
values = sorted(roman_numerals.keys(), reverse=True)

#     # Initialize the result
#     roman_string = ''
#
#     # Loop through the values and build the Roman numeral string
#     for value in values:
#         while num >= value:
#             roman_string += roman_numerals[value]
#             num -= value
#
#     return roman_string
#
#
# # Example usage
# num = 1994
# print(f"The Roman numeral for {num} is {int_to_roman(num)}")
