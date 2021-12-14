'''
hex_to_rgb
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
