###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
# s
swift = input('daj kod swift: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
print(f'Location Code: {swift[6:8]}')
