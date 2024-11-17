###
# A program that prints your height both in cm and in feet and inches.
#
cm = 180
inches = cm / 2.54
# calculate the number of feet

feet = cm / 30.48
inches = inches % 12
print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {int(inches)} inches')
