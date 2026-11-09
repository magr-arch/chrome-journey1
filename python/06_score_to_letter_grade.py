# Score to Letter Grade Python Exercise
# MAGR ^-^
# 2026-11-08

"""Report the letter grade for a given score.

The relation for score to letter grade is as follows.

Score	  | Grade
----------|----------
90-100	  |   A
80-89.99  |   B
70-79.99  |	  C
60-69.99  |	  D
below 60  |	  F

If any score above 100 or below 0 is entered it will be an invalid score.
"""

score = float(input("Enter your score (0-100): "))
print("-" * 40)

if score < 0 or score > 100:
    print("invalid score.")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score: {score:.1f} -> Grade: {grade}")
    
print("-" * 40)
