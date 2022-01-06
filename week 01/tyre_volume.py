import math
from datetime import datetime

w = float(input("Enter the width of the tire in mm (ex 205):"))
a = float(input("Enter the aspect ratio of the tire (ex 60):"))
d = float(input("Enter the diameter of the wheel in inches (ex 15):"))

calc1 = math.pi * w * w * a
calc2 = w * a + 2540 * d

volume = round(calc1 * calc2/10000000000, 4)

print(f"The approximate volume is {volume} liters")
answer = input(f"Would like to buy a tyre with {d}? (Type y/n)")

if answer == "y":
    phone = input("Please, enter you phone number. We will get in contact soon.")

currentDateTime = datetime.now()

with open("volumes.txt", "at") as volumesFile:
    print(f"", file=volumesFile)
    print(f"----------------------------", file=volumesFile)
    print(currentDateTime, file=volumesFile)
    print(f"Customer's phone: {phone}", file=volumesFile)
    print(f"Width: {w}", file=volumesFile)
    print(f"Aspect Ratio: {a}", file=volumesFile)
    print(f"Diameter: {d}", file=volumesFile)
    print(f"Volume: {volume}", file=volumesFile)
    print(f"----------------------------", file=volumesFile)
    print(f"", file=volumesFile)

print(f"Thank you for using our services.")