# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.


def int_to_roman(num: int) -> str:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ''
    for value, numeral in roman_map:
        while num >= value:
            result += numeral
            num -= value
            
    return result
