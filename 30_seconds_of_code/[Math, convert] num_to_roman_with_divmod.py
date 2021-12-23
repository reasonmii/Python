
'''
to_roman_numeral
Converts an integer to its roman numeral representation
Accepts value between 1 and 3999 (both inclusive)

- Create a lookup list containing tuples in the form of (roman value, integer)
- Use a for loop to iterate over the values in lookup
- Use divmod() to update num with the remainder, adding the roman numeral representation to the result

https://www.30secondsofcode.org/python/s/to-roman-numeral
'''

def to_roman_numeral(num):
    lookup = [
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
        (1, 'I'),
        ]
    rst = ''
    for (n, roman) in lookup:
        (d, num) = divmod(num, n)
        rst += roman * d
    return rst


# Example
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'


# reference =====================================================

divmod(11, 3)  # (3, 2)
divmod(40, 4)  # (10, 0)
divmod(40, 3)  # (13, 1)
