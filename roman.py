def decimal_to_roman(decimal_number):
    """
    Converts a decimal number to Roman numerals.
    """
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    roman_numeral = ''
    for value, letter in roman_numerals:
        while decimal_number >= value:
            roman_numeral += letter
            decimal_number -= value
    return roman_numeral

# Prompt the user to enter a decimal number
decimal_number = int(input('Enter a decimal number: '))

# Convert the decimal number to Roman numerals
roman_numeral = decimal_to_roman(decimal_number)

# Display the Roman numeral
print(f'{decimal_number} in Roman numerals is {roman_numeral}')

