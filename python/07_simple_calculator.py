# Simple Calculator Python Exercise
# MAGR ^-^
# 2026-11-09

"""Add, subtract, multiply or divide two numbers.

The script asks for two numbers and an operator (+, -, *, /) and
prints the result of the operation.

An invalid operator or a division by zero is reported with a message
instead of a result.
"""

print("Simple Calculator: add, subtract, multiply or divide")
print("-" * 40)

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator not in ("+", "-", "*", "/"):
    print("Invalid operator.")
elif operator == "/" and number2 == 0:
    print("Cannot divide by zero.")
else:
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    else:  # Only "/" is left, because the operator was already validated.
        result = number1 / number2
    print(f"{number1} {operator} {number2} = {result}")
    print("-" * 40)
