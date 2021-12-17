'''
camel
Converts a string to camelcase

- Use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+"
- Use str.title() to capitalize the first letter of each word and convert the rest to lowercase
- Finally, use str.replace() to remove spaces between words

CamelCase
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ege1001&logNo=220466932974
- 단어가 합쳐진 부분마다 맨 처음 글자를 대문자로 표기하는 방법
- 두 개 이상의 단어가 모인 합성어에서 사용
- 쌍봉낙타의 등과 닮았다고 해서 이렇게 이름이 붙음

1) lowerCamelCase
- 맨 앞글자를 소문자로 표기
- 나머지 뒤에 따라붙는 단어들의 앞글자는 모두 대문자로 표기
- ex) namuWikiReflecBeatComponent, beatMania

2) UpperCamelCase (=PascalCase)
- 맨 앞글자를 대문자로 표기
- 나머지 뒤에 따라붙는 단어들의 앞글자는 모두 대문자로 표기
- ex) NamuWikiReflecBeatComponent, BeatMania

https://www.30secondsofcode.org/python/s/camel
'''

import re

def camel(s):
    s = re.sub(r'(-|_)+'," ",s).title().replace(" ", "")
    # 첫 시작 글자만 다시 소문자로 변경, 이후 문자는 그대로
    return ''.join([s[0].lower(), s[1:]])


# Example
camel('some_database_field_name') # 'someDatabaseFieldName'
camel('Some label that needs to be camelized')
# 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property') # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens')
# 'someMixedStringWithSpacesUnderscoresAndHyphens'


# reference =====================================================

# title : 첫 글자를 모두 대문자로 변경
('hellow world').title()  # 'Hellow World'

a = 'some_database_field_name'
re.sub(r'(-|_)+'," ",a)                           # 'some database field name'
re.sub(r'(-|_)+'," ",a).title()                   # 'Some Database Field Name'
re.sub(r'(-|_)+'," ",a).title().replace(" ","")   # 'SomeDatabaseFieldName'


