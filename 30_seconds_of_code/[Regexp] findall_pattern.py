
'''
words
Converts a given string into a list of words

- Use re.findall() with the supplied pattern to find all matching substrings
- Omit the second argument to use the default regexp, which matches alphanumeric and hyphens

정규표현식 Regular Expression
https://hamait.tistory.com/342
1) \b : word boundary를 표현하며 문자와 공백사이의 문자를 의미
2) \B : non word boundary를 표현하며 문자와 공백사이가 아닌 문자를 의미
3) [a-zA-Z-] : 'A-Z' 뒤에 -가 붙으면 one-time 같이 '-'로 연결된 경우, 하나의 단어로 인식

https://www.30secondsofcode.org/python/s/words
'''

import re

def words(s, pattern = '[a-zA-Z-]+'):
    return re.findall(pattern, s)
  

# Example
words('I love Python!!') # ['I', 'love', 'Python']
words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']


# reference =====================================================

# re.findall(pattern, string, flags)
# 문자열 중 패턴과 일치되는 모든 부분 찾음

print(re.findall('a', 'aba'))      # ['a', 'a']
print(re.findall('a', 'bbb'))      # []
print(re.findall('a', 'baa'))      # ['a', 'a']
print(re.findall('aaa', 'aaaa'))   # ['aaa']

