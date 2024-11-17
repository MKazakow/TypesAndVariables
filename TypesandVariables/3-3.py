###
# A program for swapping two varable values
# Two variables x and y have values of 7 and 34. Write a program that swaps variable values (x should be 34 and y should be 7). Use an additional, auxiliary variable.
x = 7
y = 34
z = 0  # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)
