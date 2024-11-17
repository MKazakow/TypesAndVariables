import random
dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)
dice_roll_4 = random.randint(1, 6)
isspecial = dice_roll_1 == 1 or dice_roll_1 == 6 or dice_roll_2 == 1 or dice_roll_2 == 6 or dice_roll_3 == 1 or dice_roll_3 == 6 or dice_roll_4 == 1 or dice_roll_4 == 6

print(f"Dice rolled: 4")
print(f"Special number: {isspecial}")
