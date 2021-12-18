
'''
slugify
Converts a string to a URL-friendly slug

- Use str.lower() and str.strip() to normalize the input string
- Use re.sub() to to replace spaces, dashes and underscores with -
  and remove special character

★ slugify
- A slug is a human-readable, unique identifier, used to identify a resource
  instead of a less human-readable identifier like an id
- You use a slug when you want to "refer to an item"
  while preserving the ability to see, at a glance, what the item is

strip([chars])
- String의 왼쪽과 오른쪽 공백 제거

정규표현식
- ^ : 문자열의 시작 의미
- \w : word, 알파벳, 숫자, _
- \s : space, 공백문자
- $ : 문자열의 종료 의미

https://www.30secondsofcode.org/python/s/slugify
'''

from re import sub

def slugify(s):
    s = s.lower()
    s = sub(r'[^\w\s-]', '', s)   # 특수문자 -> 삭제
    s = sub(r'[\s_-]+', '-', s)   # '_' or '--' -> -
    s = sub(r'^-+|-+$', '', s)    # 시작문자 '-' or 마지막문자 '-' -> 삭제
    return s

            
# Example
slugify('Hello World!')           # 'hello-world'
slugify('___This is a test ---')  # 'this-is-a-test'


# reference =====================================================

s = '-hello_world-tick*$^tock--123+-'

sub(r'[^\w\s-]', '', s)
# '-hello_world-ticktock--123-'
# 특수문자 -> ''

sub(r'[\s_-]+', '-', s)
# '-hello-world-tick*$^tock-123+-'
# '_' or '--' -> '-'

sub(r'^-+|-+$', '', s)
# 'hello_world-tick*$^tock--123+'
