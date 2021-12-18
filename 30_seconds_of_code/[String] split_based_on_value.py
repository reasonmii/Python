
'''
split_lines
Splits a multiline string into a list of lines

- Use str.split() and '\n' to match line breaks and create a list
- str.splitlines() provides similar functionality to this snippet

https://www.30secondsofcode.org/python/s/split-lines
'''

def split_lines(s):
    return s.split('\n')


# Example
split_lines('This\nis a\nmultiline\nstring.\n')
# ['This', 'is a', 'multiline', 'string.' , '']
