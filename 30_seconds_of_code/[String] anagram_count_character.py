
'''
is_anagram
Checks if a string is an anagram of another string
(case-insensitive, ignores spaces, punctuation and special characters)

- Use str.isalnum() to filter out non-alphanumeric characters,
  str.lower() to transform each character to lowercase
- Use collections.Counter to count the resulting characters
  for each string and compare the results

isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어있으면 True, 아니면 False

https://www.30secondsofcode.org/python/s/is-anagram
'''

from collections import Counter

def is_anagram(s1, s2):
    return Counter(c.lower() for c in s1 if c.isalnum()) == Counter(c.lower() for c in s2 if c.isalnum())
    

# Example
is_anagram('#anagram', 'Nag a ram!')  # True


# reference =====================================================

s1 = 'apple'
Counter(c.lower() for c in s1 if c.isalnum())
# Counter({'a': 1, 'p': 2, 'l': 1, 'e': 1})

