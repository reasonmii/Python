'''
Python's f-strings provide a more readable, concise and less error-prone way to format strings
- https://www.30secondsofcode.org/articles/s/6-python-f-strings-tips
- https://www.30secondsofcode.org/articles/s/python-fstrings-str-format

Formatted string literals, commonly known as f-strings, are strings prefixed with 'f' or 'F'

1. String Interpolation
- The most used f-string feature by far
- Just wrap the value or variable in curly braces ({})
'''

str_val = 'apples'
num_val = 42
print(f'{num_val} {str_val}') # 42 apples

'''
2. Variable names
- This can be especially useful when debugging
- It can beeasily accomplished by adding an equals sign (=)
- ★ Whitespace inside the curly braces is taken into account,
  so adding spaces around the equals sign can make for a more readable result
'''

str_val = 'apples'
num_val = 42
print(f'{str_val=}, {num_val = }') # str_val='apples', num_val = 42

'''
3. Mathematical operations
- Place the mathematical expression inside the curly braces
- If you add an equal sign, you'll get the expression and its result
'''

num_val = 42
print(f'{num_val % 2 = }')  # num_val % 2 = 0

'''
4. Printable representation
- Use the repr() function
- A much shorter syntax by appending a !r inside the curly braces
'''

str_val = 'apples'
print(f'{str_val!r}') # 'apples'

'''
5. Number formatting
- To add formatting to a value you can add a colon (:) followed by a format specifier
- This can also be combined with the equals sing from before,
  shall you want to print the name of the variable as well
- To trim a numeric value to two digits after the decimal, you can use the .2f format specifier
'''

price_val = 6.12658
print(f'{price_val:.2f}') # 6.13

'''
6. Date formatting
- %Y denotes the full year, %m is the month and %d is the day of the month
'''

from datetime import datetime;
date_val = datetime.utcnow()
print(f'{date_val=:%Y-%m-%d}') # date_val=2021-07-09


