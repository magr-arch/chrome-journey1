# RPM to Rad/s Python Exercise
# MAGR ^-^
# 2026-11-10

"""RPM to Rad/s convertor.

Input: Speed value in RPM.

RPM to Rad/s formula:

  rpm x 2π rad/rev x 1 min/60 s = rad/s

  rad/s = rpm x 2π / 60

  
"""

import math

SECONDS_PER_MINUTE = 60

print("Convert RPM into Rad/s or Rad/s to RPM.")
print("-" * 40)

operator = input("Chose the Operation (RPM>RAD / RAD>RPM): ")

if operator not in ("RPM>RAD", "RAD>RPM"):
    print("Invalid operator.")
else:
    if operator == "RPM>RAD":   
        rpm = float(input("Enter speed in RPM: "))
        rad_per_s = rpm * (2*math.pi)/SECONDS_PER_MINUTE
        print(f"{rpm} rpm = {rad_per_s:.2f} rad/s")
    else:
        rad_per_s = float(input("Enter speed in rad/s: "))
        rpm = rad_per_s * SECONDS_PER_MINUTE/(2*math.pi) 
        print(f"{rad_per_s} rad/s = {rpm:.2f} rpm")
    print("-" * 40)
