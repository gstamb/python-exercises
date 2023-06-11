# Exercise: https://www.hackerrank.com/challenges/find-angle
import math

a = int(input())
b = int(input())

tangent = a / b
angle = math.atan(tangent)

angle_degrees = math.degrees(angle)
print(f"{int(round(float(angle_degrees),0))}{chr(176)}")