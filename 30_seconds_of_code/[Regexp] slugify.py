
'''
1) slugify
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


'''
2) kebab
Converts a string to kebab case

- Use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+"
- Use re.sub() to match all words in the string, str.lower() to lowercase them
- Finally, use str.join() to combine all word using - as the separator

정규표현식 Regular Expression
https://wikidocs.net/4308
1) \s
   whitespace 문자와 매치
   [ \t\n\r\f\v]와 동일한 표현식
   맨 앞의 빈 칸은 공백문자(space)를 의미
2) ? : 0~1회 일치
3) 반복 (+) : 1번 이상
4) 반복 (*) : 0번 이상
5) 반복 ({m,n}, ?)
   {1,}은 +와 동일, {0,}은 *와 동일
   ex) ca{2}t : a 반드시 두 번 반복
   ex) ca{2,5}t : a 2~5번 반복

https://www.30secondsofcode.org/python/s/kebab
'''

from re import sub

def kebab(s):
    return '-'.join(
        sub(r'(\s|_|-)+'," ",
            sub(r'[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+',
                lambda mo: ' ' + mo.group(0).lower(), s)).split())
  

# Example
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'


# reference =====================================================

### re.sub（정규 표현식, 대상 문자열 , 치환 문자

s = '-hello_world-tick*$^tock--123+-'

sub(r'[^\w\s-]', '', s)
# '-hello_world-ticktock--123-'
# 특수문자 -> ''

sub(r'[\s_-]+', '-', s)
# '-hello-world-tick*$^tock-123+-'
# '_' or '--' -> '-'

sub(r'^-+|-+$', '', s)
# 'hello_world-tick*$^tock--123+'

import re
text = "I like apble And abple"
text_mod = re.sub('apble|abple',"apple",text)
print (text_mod)  # I like apple And apple

### 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 반환
a = 'abcdef\n'
print(a)   # abcdef

b = r'abcdef\n'
print(b)   # abcdef\n

###
sub(r'(\s|_|-)+'," ","abc-def_ghi jkl")   # 'abc def ghi jkl'

