from datetime import datetime


def main():
    
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    height = float(input("Enter your height in U.S. pounds: "))
    pounds = float(input("Enter your weight in U.S. inches: "))

  
    age = compute_age(birthdate)
    weight = kg_from_lb(pounds)
    heightCm = cm_from_in(height)
    bmi = body_mass_index(weight, heightCm)
    bmr = basal_metabolic_rate(gender, weight, heightCm, age)

    # Print the results for the user to see.
    print("----------------------------------------")
    print(f"Age (years): {age}")
    print(f"Weight (kg): {round(weight, 2)}")
    print(f"Height (cm): {round(heightCm,2)}")
    print(f"Body mass index: {round(bmi, 2)}")
    print(f"Basal metabolic rate (kcal/day): {round(bmr, 2)}")
    print("----------------------------------------")


def compute_age(birth):

    birth = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

   
    years = today.year - birth.year

 
    if birth.month > today.month or \
        (birth.month == today.month and \
            birth.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):

    return  pounds * 0.45359237



def cm_from_in(inches):
  
    return inches * 2.54


def body_mass_index(weight, height):

    return 10000 * weight / height * height


def basal_metabolic_rate(gender, weight, height, age):
 
    if gender == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
        return bmr

    elif gender ==  "M":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        return bmr

    else: 
        print("Your code for gender is not valid. Please, type M or F.")
        main()


main()