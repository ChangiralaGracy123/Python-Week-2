# Filename: Magic date.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: A program that checks whether the date is magic or not
# Last changed: 05-02-2024

# To determine the date of the program is magic or not

# Get user input for the numeric month, day, and two-digit year
MM = int(input("Enter the numeric month: "))
DD = int(input("Enter the day: "))
YY = int(input("Enter the two-digit year: "))

# Check if the product of month and day equals the year
if MM * DD == YY:
    print("The date is magic!")
else:
    print("The date is not magic.")

# Description:
# This program takes user input for the numeric month (M), day (D), and two-digit year (Y).
# It then checks whether the product of the month and day equals the entered two-digit year.
# If the product is equal to the year, the program prints a message indicating that the date is magic.
# Otherwise, it prints a message stating that the date is not magic.
