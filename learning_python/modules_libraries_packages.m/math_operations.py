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

def exponentiate(base, exponent):
    return base ** exponent


def evaluate_expression(expression):
    def parse_expression(expr):
        stack = []
        num = 0
        sign = 1
        result = 0
        i = 0

        while i < len(expr):
            char = expr[i]

            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
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
            elif char == ')':
                result += sign * num
                return result
            i += 1

        result += sign * num
        return result

    return parse_expression(expression)
