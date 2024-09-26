"""Python comments to help to achieve the MVP (minimum viable product):
BMI:
Metric system: weight (kg) height (m)  squared: weight/ squared height
Imperial system: weight (lbs) height (in) squared: weight / squared height * 703

- Get the user's height and weight
- Calculate their BMI from the height and weight given
- Print the BMI as a message to the user

If time, create a version 2 with some of your own ideas"""

"""Metric System"""
mertic_system = input("Hello, we will be calculating your BMI using the metric system. (Entr to continue)")
height = float(input("Enter your height in (m): "))
weight = float(input("Enter your weight in (kg): "))

height = height * height
bmi = round(weight / height, 2)

print(f"Your BMI is: {bmi}.")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are in the healthy weight range.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")


"""Imperial System"""
imperial_system = input("Hello, we will be calculating your BMI using the imperial system. (Entr to continue)")
height = float(input("Enter your height in (in): "))
weight = float(input("Enter your weight in (lbs): "))

height = height * height
bmi = round((weight / height) * 703,2)

print(f"Your BMI is: {bmi}.")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are in the healthy weight range.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")