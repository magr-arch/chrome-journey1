# Temperature Convertor Python Exercise
# MAGR
# 04/11/2026
"""
celsius to fahrenheit Formula

°F = (°C x 9/5) + 32

fahrenheit to celsius Formula

°C = (°F - 32) x 5/9

"""

print("Insert fahrenheit and celsius values to see they're conversion from one another")
print("_______________________________________________________________________________")

# fahrenheit to celsius

print("Try with fahrenheit to celsius")

fahrenheit = float(input("fahrenheit value: "))

celsius = (fahrenheit - 32) * 5/9

print(f"the conversion from {fahrenheit}°F to celsius is {celsius:.2f}°C")
print("______________________________________________")


# celsius to fahrenheit

print("Now try celsius to fahrenheit")

celsius = float(input("celsius value: "))

fahrenheit = (celsius * 9/5) + 32

print(f"the conversion from {celsius}°C to fahrenheit is {fahrenheit:.2f}°F")
