# RPM to Rad/s Python Exercise
# MAGR ^-^
# 2026-11-10

"""RPM to Rad/s convertor

Input: Speed value in RPM

RPM to Rad/s formula

rpm x 2π rad/rev x 1 min/60 s = rad/s

rad/s rpm x 2π / 60
"""

import math

SECONDS_PER_MINUTE: 60

print("Convert RPM into Rad/s")
print("-" * 40)

rpm = float(input("Enter speed in RPM: "))

rad_per_s = rpm * (2*math.pi)/60

print(f"{rpm} rpm = {rad_per_s:.2f} rad/s")
print("-" * 40)
