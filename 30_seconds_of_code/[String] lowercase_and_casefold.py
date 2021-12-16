'''
https://www.30secondsofcode.org/articles/s/python-lowercase

str.lower()
- It is compatible with both Python 2 and Python 3
- Standard way for most cases
- There are certain cases where this method might not be the most appropriate,
  ★ especially if you are working with Unicode strings.
'''

'Hello'.lower()               # 'hello'
'Straße'.lower()              # 'straße'
'Straße'.upper().lower()      # 'strasse'

# Example of incorrect result when used for unicode case-insensitive matching
'Straße'.upper().lower() == 'Straße'.lower()  # False ('strasse' != 'straße')

'''
str.casefold()
- Python 3 introduced str.casefold()
- Very similar to str.lower()
- More aggressive as it is intended to "remove all case distinctions in Unicode strings"
'''

'Hello'.casefold()            # 'hello'
'Straße'.casefold()           # 'strasse'
'Straße'.upper().casefold()   # 'strasse'

# Returns the correct result when used for unicode case-insensitive matching
'Straße'.upper().casefold() == 'Straße'.casefold() # True
