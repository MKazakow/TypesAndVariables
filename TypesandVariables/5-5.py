#
# The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the product price and discount. Print the product price, discount, discounted product price, and the difference between the product price before and after the discount. Print all prices with two decimal places
#

entry_price = input("Podaj cenę początkową: ")
discount = input("Podaj wysokość zniżki w %: ")
entry_price = float(entry_price)
discount = float(discount)
reduction = entry_price * discount / 100
price_after_discount = entry_price - reduction
print(f"Enter price: {entry_price: .2f}")
print(f"Enter discount: {int(discount)}%")
print(f"Price with discount: {price_after_discount: .2f}")
print(f"Reduction: {reduction: .2f}")
