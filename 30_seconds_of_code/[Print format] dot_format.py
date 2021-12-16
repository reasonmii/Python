'''
The str.format() method works very much alike f-strings
The main difference being that replacement fields are "supplied as arguments"

https://www.30secondsofcode.org/articles/s/python-fstrings-str-format
'''

name = 'John'
age = 32

print('{0} is {1} years old'.format(name, age)) # 'John is 32 years old'

