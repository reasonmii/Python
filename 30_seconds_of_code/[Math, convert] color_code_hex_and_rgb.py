'''
1) hex_to_rgb
Converts a hexadecimal color code to a tuple of integers corresponding to its RGB components.

- Use a list comprehension in combination with int()
  and list slice notation to get the RGB components from the hexadecimal string
- Use tuple() to convert the resulting list to a tuple

https://www.30secondsofcode.org/python/s/hex-to-rgb
'''

def hex_to_rgb(hex):
    # int('FF', 16) : 'FF'를 16진수 인지하고, int로 변경
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


# Example
hex_to_rgb('FFA501') # (255, 165, 1)


'''
2) rgb_to_hex
Converts the values of RGB components to a hexadecimal color code

- Create a placeholder for a zero-padded hexadecimal value
  using '{:02X}' and copy it three times.
- Use str.format() on the resulting string
  to replace the placeholders with the given values
  
https://www.30secondsofcode.org/python/s/rgb-to-hex
'''

def rgb_to_hex(r, g, b):
    return ('{:02X}' * 3).format(r, g, b)


# Example
rgb_to_hex(255, 165, 1) # 'FFA501'
