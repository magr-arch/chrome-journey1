# Circle Area and Perimeter Python Exercise
# MAGR ^-^
# 04/11/2026

"""
circle area and perimeter formulas

area: pi x r^2
______________________________

perimeter: 2 x pi x r
______________________________

r = radius

pi = math.pi (3.14159)

"""
import math

print("get the area and perimeter of any circle by inputing its radius value below")
print("____________________________________________________________________________")

radius = float(input("input the radius (m): "))
print("____________________________________________________________________________")

area = math.pi * radius**2

perimeter = 2 * math.pi * radius

print(f"the area of the circle is {area:.2f} m^2")
print(f"the perimeter of the circle is {perimeter:.2f} m")