"""
You work for a retail store that wants to increase 
sales on Tuesday and Wednesday, which are the store's 
slowest sales days. On Tuesday and Wednesday, 
if a customer's subtotal is $50 or greater, the store 
will discount the customer's subtotal by 10%.
"""
from datetime import datetime

subtotal = float(input("Please, inform the subtotal"))

currentDateTime = datetime.now()
dayOfWeek = currentDateTime.weekday()

if subtotal > 50 and (dayOfWeek == 1 or dayOfWeek) == 2 :
    discount = subtotal * 0.1
    subtotal = subtotal - discount
    salesTax = subtotal * 0.06
    total = subtotal + salesTax
else:
    discount = 0
    salesTax = subtotal * 0.06
    total = subtotal + salesTax

print(f"---------------------------------------")
print(f"Discount: ${round(discount, 2)} ")
print(f"Sales Tax: ${round(salesTax, 2)} ")
print(f"Total: ${round(total, 2) } ")
print(f"---------------------------------------")