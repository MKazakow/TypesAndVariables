

# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:
speed = input("Podaj prędkość: ")
speed = float(speed)
iscorrect = speed <= 140 and speed >= 40
print(f"Speed is valid: {iscorrect}")
