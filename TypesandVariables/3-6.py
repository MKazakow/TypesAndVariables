# Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:
#
#
#
#
import math

h = input("podaj wysokość w metrach: ")
h = float(h)
d = 3.57 * math.sqrt(h)
print("Odległość od horyzontu: ", d, "km")
