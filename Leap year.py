# Filename: Leap year.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to check if a year is a leap year
# Last changed: 05-02-2024

# Determine the program if a year is a leap year

# Get user input for the year
y = int(input("Enter a year: "))

# Check the conditions for a leap year
if y % 400 == 0:
    print(f"{y} is a leap year.")
elif y % 100 == 0:
    print(f"{y} is not a leap year.")
elif y % 4 == 0:
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")

# Description:
# We start by getting a year as input from the user.
# The first if statement checks if the year is divisible by 400, and if true, prints that it is a leap year.
# The elif (else if) statement checks if the year is divisible by 100, and if true, prints that it is not a leap year.
# If neither of the above conditions is met, the next elif statement checks if the year is divisible by 4, and if true, prints that it is a leap year.
# If none of the conditions are met, it means the year is not divisible by 400, 100, or 4, and the else statement prints that it is not a leap year.
