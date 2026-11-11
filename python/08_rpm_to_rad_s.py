# RPM to Rad/s Python Exercise
# MAGR ^-^
# 2026-11-10

"""Convert a rotational speed between rpm and rad/s.

The script asks for a conversion option, then for the speed to convert:

    rad/s = rpm * 2 * pi / 60
    rpm = rad/s * 60 / (2 * pi)

Negative speeds are accepted and mean rotation in the opposite
direction. An invalid option is reported with a message.
"""

import math

SECONDS_PER_MINUTE = 60
RADIANS_PER_REVOLUTION = 2 * math.pi

print("Convert RPM into Rad/s or Rad/s to RPM.")
print("-" * 40)

mode = input("RPM > RAD: 1 / RAD > RPM: 2): ")

if mode not in ("1", "2"):
    print("Invalid operator.")
else:
    if mode == "1":   
        rpm = float(input("Enter speed in RPM: "))
        rad_per_s = rpm * RADIANS_PER_REVOLUTION/SECONDS_PER_MINUTE
        print(f"{rpm:.2f} rpm = {rad_per_s:.2f} rad/s")
    else:  # Only "RAD > RPM" is left
        rad_per_s = float(input("Enter speed in rad/s: "))
        rpm = rad_per_s * SECONDS_PER_MINUTE/RADIANS_PER_REVOLUTION 
        print(f"{rad_per_s:.2f} rad/s = {rpm:.2f} rpm")
    print("-" * 40)
