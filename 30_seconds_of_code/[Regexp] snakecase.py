
'''
snake
Converts a string to snake case

- Use re.sub() to match all words in the string, str.lower() to lowercase them
- Use re.sub() to replace any - characters with spaces
- Finally, use str.join() to combine all words using - as the separator

\1 is equivalent to re.search(...).group(1)
- the first parentheses-delimited expression inside of the regex

https://www.30secondsofcode.org/python/s/snake
'''

import re

def snake(s):
    s = s.replace('-', ' ')
    s = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', s)).split()
    return '_'.join(s).lower()


# Example
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'


# reference =====================================================

a = 'some-mixed_string With spaces_underscores-and-hyphens'

a = a.replace('-', ' ')
# 'some mixed_string With spaces_underscores and hyphens'

a = re.sub('([A-Z]+)', r'\1', a)
# 'some mixed_string With spaces_underscores and hyphens'

a = re.sub('([A-Z][a-z]+)', r'\1', a).split()
# ['some', 'mixed_string', 'With', 'spaces_underscores', 'and', 'hyphens']

'_'.join(a).lower()
# 'some_mixed_string_with_spaces_underscores_and_hyphens'

b = 'camelCase'
b = b.replace('-', ' ')
b = re.sub('([A-Z]+)', r' \1', b)                # 'camel Case'
b = re.sub('([A-Z][a-z]+)', r' \1', b).split()   # ['camel', 'Case']
'_'.join(b).lower()                              # 'camel_case'


