###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# input temperature in celsius
celsius = input("Podaj temperature w stopniach celsjusza ")
celsius = float(celsius)
# calculate farenheit and kelvin
fahrenheit = 2*celsius + 32
kelvin = celsius + 273
# printing results
print(f"Temperatura w kelvinach: {kelvin}")
print(f"Temperatura w fahrenheitach: {fahrenheit}")
