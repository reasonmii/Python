'''
palindrome
Checks if the given string is a palindrome

- Use str.lower() and re.sub() to convert to lowercase
  and remove non-alphanumeric characters from the given string
- Compare the new string with its reverse, using slice notation

re.sub（정규 표현식, 대상 문자열 , 치환 문자）
- 정규 표현식 - 검색 패턴
- 대상 문자열 - 검색 대상이 되는 문자열
- 치환 문자 - 변경하고 싶은 문자

\W
- 문자+숫자(alphanumeric)가 아닌 것
- [^a-zA-Z0-9_]와 동일한 표현식

https://www.30secondsofcode.org/python/s/palindrome
'''

import re

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]


# Example
palindrome('taco cat') # True
