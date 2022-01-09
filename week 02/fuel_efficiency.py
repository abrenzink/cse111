def main():
    startOdometer = int(input("Inform the starting odometer value in miles:"))
    endOdometer = int(input("Inform the ending odometer value in miles:"))
    fuel = float(input("Inform the amount of fuel in gallons:"))

    mpg = round(miles_per_gallon(startOdometer, endOdometer, fuel), 1)
    lp100k = round(lp100k_from_mpg(mpg), 2)

    print(f"{mpg} miles per gallon")
    print(f"{lp100k} miles per gallon")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
   
    return (end_miles - start_miles)/amount_gallons

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return 235.215/mpg

main()