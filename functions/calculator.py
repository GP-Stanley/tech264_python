
"""complete a viable basic calculator using functions.
MVP (each of these should be in a separate function):
* Can add 2 numbers
* Can subtract 2 numbers
* Can multiply 2 numbers
* Can divide 2 numbers
 """

# mini calculator.
def add(x, y):
    return x + y

# Function to subtract two numbers.
def subtract(a, b):
    return a - b

# Function to multiply two numbers.
def multiply(a, b):
    return a * b

# Function to divide two numbers.
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# to the power of
def exponentiate(base, exponent):
    return base ** exponent


def evaluate_expression(expression):                # takes a mathematical expression as a string and evaluates it.
    def parse_expression(expr):                     # does the parsing and evaluation of the expression.
        stack = []                                  # stack: used for handling nested expressions.
        num = 0                                     # stores the current number being processed.
        sign = 1                                    # stores the current sign (1 = pos, -1 = neg).
        result = 0                                  # accumulates the result of the expression.
        i = 0                                       # index: to traverse the expression string.

        while i < len(expr):                        # this loop iterates through each character in the expression (expr).
            char = expr[i]

            if char.isdigit():                      # digit handling: If the character is a digit, it updates num by shifting the current num left by one decimal place (multiplying by 10) and adding the new digit.
                num = num * 10 + int(char)
            elif char == '+':                       # addition handling: If the character is a ‘+’, it adds the current num to result (considering the current sign), resets num to 0, and sets sign to 1 (positive).
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':                       # subtraction handling: If the character is a ‘-’, it adds the current num to result (considering the current sign), resets num to 0, and sets sign to -1 (negative).
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':                       # paranthesis handling: If the character is ‘(’, it finds the corresponding closing ‘)’ by maintaining a balance counter. It then recursively evaluates the expression inside the parentheses using parse_expression.
                j = i
                balance = 0
                while i < len(expr):
                    if expr[i] == '(':
                        balance += 1
                    if expr[i] == ')':
                        balance -= 1
                    if balance == 0:
                        break
                    i += 1
                num = parse_expression(expr[j + 1:i])
            elif char == ')':                           # closing paranthesis handling: If the character is ‘)’, it adds the current num to result and returns result.
                result += sign * num
                return result
            i += 1                                      # increment index: Moves to the next character in the expression.

        result += sign * num                            # final addition: After the loop, it adds the last num to result and returns result.
        return result

    return parse_expression(expression)                 # entry point: This is the entry point of the function, which starts the parsing process.


"""
This code essentially evaluates a mathematical expression by parsing it character by character, 
handling digits, operators, and parentheses appropriately. 
"""

"""
Taking it to the next level: 
* Implement more complex operations, such as handling parentheses, exponentiation 
* More advanced operations should continue to be broken into separate functions 
"""


# User input for each function
def main():
    while True:
        print("\nMini Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Evaluate Expression")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {add(x, y)}")

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {subtract(a, b)}")

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {multiply(a, b)}")

        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {divide(a, b)}")

        elif choice == '5':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print(f"Result: {exponentiate(base, exponent)}")

        elif choice == '6':
            expression = input("Enter expression: ")
            print(f"Result: {evaluate_expression(expression)}")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()



print("------------------------------------------------------------------------------")
"""Taking it to the next level: 
* Implement more complex operations, such as handling parentheses, exponentiation 
* More advanced operations should continue to be broken into separate functions 
"""

def calculator():
    operation = input("Choose an operator (+, -. *, /): ")
    num1 = float(input("Enter a numer: "))
    num2 = float(input("Enter a number: "))

    if operation == "+":
        print(add(num1, num2))

    elif operation == "-":
        print(subtract(num1, num2))

    elif operation == "*":
        print(multiply(num1, num2))

    elif operation == "/":
        print(divide(num1, num2))
    else:
        print("Error.")