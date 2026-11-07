# Number Sign Python Exercise
# MAGR ^-^
# 2026-11-07

"""Report whether a number is positive, negative or zero.

The script asks for a number and uses an if/elif/else statement
to print its sign.
"""

number = float(input("Enter a number: "))
print("-" * 40)

if number > 0:
    print("This number is positive.")
elif number < 0:
    print("This number is negative.")
else:
    print("this number is zero.")

print("-" * 40)
