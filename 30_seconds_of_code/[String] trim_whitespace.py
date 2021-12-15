'''
How do I trim whitespace from a string in Python?
https://www.30secondsofcode.org/articles/s/python-trim-whitespace

Whitespace characters
- space ( )
- tab (\t)
- newline (\n) : 개행문자 (다음 행으로 바꿈)
- carriage return characters (\r) : 개행문자 (커서를 행의 앞으로 이동)
'''

# Remove leading and trailing whitespace characters
'  Hello  '.strip()   # 'Hello'

# Remove leading whitespace characters
'  Hello  '.lstrip()   # 'Hello  '

# Remove trailing whitespace characters
'  Hello  '.rstrip()   # '  Hello'


