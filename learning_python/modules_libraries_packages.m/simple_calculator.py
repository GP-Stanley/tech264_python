from math_operations import*

# ^^ from <module> (a single file), import the functions.
# a library is a set of modules (files).
# a module is a single file imported.
# a package is installable. A module or a library can become a package if its installable.

# Mini-calculator

# first_num = int(input("Enter the first number: "))
# second_num = int(input("Enter the first number: "))
# result = add(first_num, second_num)

# print(f"{first_num} + {second_num} = {result}")

            # 'mo' mean module.
                                        # This part assigns the alias mo to the math_operations module.
                                        # With this name, you can call functions using the shorter name, like mo.add(5, 3).





# Main program to perform operations based on user input.
def main():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))

    print(f"{first_num} + {second_num} = {add(first_num, second_num)}")
    print(f"{first_num} - {second_num} = {subtract(first_num, second_num)}")
    print(f"{first_num} * {second_num} = {multiply(first_num, second_num)}")
    print(f"{first_num} / {second_num} = {divide(first_num, second_num)}")

if __name__ == "__main__":                # ensures that the main() function runs when the script is executed directly.
    main()