import math

w = float(input("Enter the width of the tire in mm (ex 205):"))
a = float(input("Enter the aspect ratio of the tire (ex 60):"))
d = float(input("Enter the diameter of the wheel in inches (ex 15):"))

calc1 = math.pi * w * w * a
calc2 = w * a + 2540 * d

volume = round(calc1 * calc2/10000000000, 4)

print(f"The approximate volume is {volume} liters")