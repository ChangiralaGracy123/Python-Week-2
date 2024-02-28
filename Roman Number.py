# Filename: Roman Number.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program to convert a number to Roman numeral
# Last changed: 05-02-2024

#To convert a number to Roman numeral

# Get user input for the number
x = int(input("Enter a number between 1 and 10: "))

# Check if the number is within the specified range
if 1 <= x <= 10:
    # Check individual cases for Roman numerals
    if x == 1:
        print("The Roman numeral for 1 is I.")
    elif x == 2:
        print("The Roman numeral for 2 is II.")
    elif x == 3:
        print("The Roman numeral for 3 is III.")
    elif x == 4:
        print("The Roman numeral for 4 is IV.")
    elif x == 5:
        print("The Roman numeral for 5 is V.")
    elif x == 6:
        print("The Roman numeral for 6 is VI.")
    elif x == 7:
        print("The Roman numeral for 7 is VII.")
    elif x == 8:
        print("The Roman numeral for 8 is VIII.")
    elif x == 9:
        print("The Roman numeral for 9 is IX.")
    else:
        print("The Roman numeral for 10 is X.")
else:
    # Print an error message for numbers outside the specified range
    print("Error: Please enter a number between 1 and 10.")

# Description:
# We get a number as input from the user.
# The if statement checks if the number is within the specified range (1 to 10).
# Inside the if block, a series of elif (else if) statements check individual cases for Roman numerals corresponding to the entered number.
# If the entered number is not within the specified range, the else statement prints an error message.