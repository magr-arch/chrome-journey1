# Score to Letter Grade Python Exercise
# MAGR ^-^
# 2026-11-07

"""


"""

score = float(input("Enter your score (0-100): "))

if score >= 90 and score <= 100:
    print(f"The score of {score} points is equal to the letter grade of A")
elif score >= 80 and score <= 89.99:
    print(f"The score of {score} points is equal to the letter grade of B")
elif score >= 70 and score <= 79.99:
    print(f"The score of {score} points is equal to the letter grade of C")
elif score >= 60 and score <= 69.99:
    print(f"The score of {score} points is equal to the letter grade of D")
elif score < 60:
    print(f"The score of {score} points is equal to the letter grade of F")
elif score < 0 or score > 100:
    print("invalid score")
