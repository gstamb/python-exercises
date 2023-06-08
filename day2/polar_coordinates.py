# Exercise: https://www.hackerrank.com/challenges/polar-coordinates

import cmath

z = complex(input())
r = abs(z)
phi = cmath.phase(z)

print(r)
print(phi)
