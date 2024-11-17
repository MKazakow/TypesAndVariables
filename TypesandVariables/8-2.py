###
# Calculation of circle area and circumference
#
import math
# determine radius and PI values
r = input("Podaj r: ")
r = float(r)

# calculate area
area = math.pi * r**2
# calculate circumference
circum = 2 * math.pi * r
# print results
print(f"""Radius: {r}
Area = {area}
Circumference = {circum}""")
