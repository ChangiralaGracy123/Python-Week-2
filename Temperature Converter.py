# Filename: Temperature Converter.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: A program that checks whether water is in a liquid, solid, or gaseous state at sea level
# Last changed: 05-02-2024

# A program that takes a temperature value in degrees Fahrenheit from the user and prints whether water is in a liquid, solid, or gaseous state at sea level

# Get user input for temperature in Fahrenheit
T = float(input("Enter temperature in degrees Fahrenheit: "))

# Check the state of water based on the given temperature
if T <= 32:
    print("At sea level, water is solid (ice) at this temperature.")
elif 32 < T < 212:
    print("At sea level, water is liquid at this temperature.")
else:
    print("At sea level, water is gaseous (steam) at this temperature.")

# Description:
# The first line of code uses the input function to obtain a user input for the temperature in Fahrenheit.
# The input is then converted to a floating-point number using float() and stored in the variable temperature_fahrenheit.
# Then lines of code use conditional statements (if, elif, else) to check the entered temperature against specific ranges.
# Based on these ranges:
# 1. If the temperature is at or below 32°F, it prints that water is in a solid state (ice) at sea level for that temperature.
# 2. If the temperature is between 32°F (exclusive) and 212°F (inclusive), it prints that water is in a liquid state at sea level for that temperature.
# 3. If the temperature is above 212°F, it prints that water is in a gaseous state (steam) at sea level for that temperature.