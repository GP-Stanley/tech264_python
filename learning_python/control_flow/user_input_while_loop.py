user_prompt = True  # remember it's a capital 'T'
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) <= 120:
        user_prompt = False
    else:
        print("Please enter a valid age (between 0 and 120).")

print(f"Your age is {age}")