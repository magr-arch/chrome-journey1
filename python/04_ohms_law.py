# Ohms Law Python Exercise
# MAGR ^-^
# 2026-11-06

"""Calculate the current in a circuit using Ohm's law.

Ohm's Law relates voltage (V), current (I) and resistance (R):

    V = I * R    ->    I = V / R

Units:
    V: volts

    I: amperes

    R: ohms

The script asks for V and R, then prints I in amperes and milliamperes.
"""

MILLIAMPS_PER_AMP = 1000

print("Ohm's law calculator: I = V / R")
print("-" * 40)

voltage = float(input("Voltage (V): "))
resistance = float(input("Resistance (ohm's): "))

if resistance == 0:
    print("Short circuit (resitance cannot be 0)")
elif resistance < 0:
    print("Invalid resitance")
else:
    current = voltage / resistance  # amperes
    current_ma = current * MILLIAMPS_PER_AMP
    print("-" * 40)
    print(f"Current: {current:.4f} A")
    print(f"Current: {current_ma:.2f} mA")
