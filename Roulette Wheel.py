# Filename: Roulette Wheel.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: A program to check the Roulette Wheel Color
# Last changed: 05-02-2024

# A program to check the Roulette Wheel Color

# Get user input for the pocket number (0 to 36)
P = int(input("Enter a pocket number (0 to 36): "))

# Check if the entered pocket number is within the valid range (0 to 36)
if 0 <= P <= 36:
    # Determine the color of the pocket based on specified rules
    if P == 0:
        print("Pocket is green.")
    elif 1 <= P <= 10 or 19 <= P <= 28:
        # Check if pocket is even or odd for red and black assignment
        if P % 2 == 0:
            print("Pocket is black.")
        else:
            print("Pocket is red.")
    elif 11 <= P <= 18 or 29 <= P <= 36:
        # Check if pocket is even or odd for red and black assignment
        if P % 2 == 0:
            print("Pocket is red.")
        else:
            print("Pocket is black.")
else:
    # Print an error message for an invalid pocket number
    print("Error: Invalid pocket number. Please enter a number between 0 and 36.")

# Description:
# This program takes user input for a pocket number on a roulette wheel (0 to 36)
# It then determines the color of the pocket based on predefined rules and displays the result.
# The program also checks for invalid input and displays an error message if the entered number is outside the valid range.
