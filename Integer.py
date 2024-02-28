# Filename: Integer.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to determine if an integer is positive, negative, or zero
# Last changed: 05-02-2024

# Determine if an integer is positive, negative, or zero

# Get user input as an integer
x = int(input("Enter an integer: "))

# Check if the user input is greater than 0
if x > 0:
    print("The integer is positive.")

# Check if the user input is less than 0
elif x < 0:
    print("The integer is negative.")

# If the above conditions are not met, the user input must be 0
else:
    print("The integer is zero.")

# Description:
# We start by getting an integer input from the user.
# The first if statement checks if the input is greater than 0, and if true, prints that the integer is positive.
# The elif (else if) statement checks if the input is less than 0, and if true, prints that the integer is negative.
# If none of the above conditions are met (i.e., the input is not greater than 0 or less than 0), it means the input must be 0, and the else statement prints that the integer is zero.