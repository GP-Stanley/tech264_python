## Task: BMI calculator
**Metric system**: weight (kg) height (m)  squared: weight/ squared height

**Imperial system**: weight (lbs) height (in) squared: weight / squared height * 703

- Get the user's height and weight
- Calculate their BMI from the height and weight given
- Print the BMI as a message to the user

If time, create a version 2 with some of your own ideas.

### Metric System Version
This is the greeting and input prompt for height and measurement.
```python
mertic_system = input("Hello, we will be calculating your BMI using the metric system. (Entr to continue)")
height = float(input("Enter your height in (m): "))
weight = float(input("Enter your weight in (kg): "))
```
BMI Calculation: the height is squared: divide weight by height: result is then rounded to two decimal places ( ,2).
```python
height = height * height
bmi = round(weight / height, 2)
print(f"Your BMI is: {bmi}.")
```
BMI Output and Classification: the BMI is printed and classified into four categories: underweight, healthy weight, overweight, or obese.
```python
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are in the healthy weight range.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
```


### Imperial System
The user is greeted and prompted to continue. Height and weight input.
```python
imperial_system = input("Hello, we will be calculating your BMI using the imperial system. (Entr to continue)")
height = float(input("Enter your height in (in): "))
weight = float(input("Enter your weight in (lbs): "))
```
BMI Calculation: height is squared. Weight divided by height, multiplied by 703.
The result is then rounded to two decimal places (, 2).
```python
height = height * height
bmi = round((weight / height) * 703,2)

print(f"Your BMI is: {bmi}.")
```
BMI Output and Classification. The BMI is printed. The BMI is classified into categories: 
underweight, healthy weight, overweight, or obese.
```python
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are in the healthy weight range.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
```