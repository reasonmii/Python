'''
1) degrees_to_rads
Converts an angle from degrees to radians

- Use math.pi and the degrees to radians formula
  to convert the angle from degrees to radians

https://www.30secondsofcode.org/python/s/degrees-to-rads
'''

from math import pi

def degrees_to_rads(deg):
    return (deg * pi) / 180.0


# Example
degrees_to_rads(180) # ~3.1416


'''
2) rads_to_degrees
Converts an angle from radians to degrees

- Use math.pi and the radian to degree formula
  to convert the angle from radians to degrees

https://www.30secondsofcode.org/python/s/rads-to-degrees
'''

from math import pi

def rads_to_degrees(rad):
    return (rad * 180.0) / pi


# Example
rads_to_degrees(pi / 2) # 90.0

