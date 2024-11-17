import math
circumference = input("Podaj obwód drzewa: ")
circumference = float(circumference)
canbe = False
diameter = circumference / math.pi
if diameter >= 50.00:
    canbe = True
print(f"Tree can be cut down: {canbe}")
