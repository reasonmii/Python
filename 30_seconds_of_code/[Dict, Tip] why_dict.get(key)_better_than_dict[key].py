'''
Tip: You should use dict.get(key) instead of dict[key]

Retrieval of dictionary values
- dict[key]
- dict.get(key)

dict.get() is usually preferred
- ★ It accepts a "second argument" which acts as the "default value"
  shall the key not exist in the given dictionary
- Due to this property, dict.get() will always return a value,
  whereas dict[key] will raise a "KeyError" if the given key is missing

https://www.30secondsofcode.org/articles/s/python-dict-getkey-vs-dictkey
'''

a = { 'max': 200 }
b = { 'min': 100, 'max': 250 }
c = { 'min': 50 }

a['min'] + b['min'] + c['min'] # throws KeyError
a.get('min', 0) + b.get('min', 0) + c.get('min', 0) # 150

