#-----------------------------------------------------------------------------
# Name:        Skipping Even Numbers (03_Skipping_Even_Number.py)
# Purpose:     Create a program that prints numbers from `1` to `10`,
#              but **skips even numbers** using the `continue` statement.
#
# Author:      LF
# Created:     17-March-2025
# Updated:     17-March-2025
#-----------------------------------------------------------------------------

print("Start")
# Looping through numbers 1 to 10
for num in range(1, 11):
    # Check if the number is even
    if num % 2 == 0:
        # Skip the even numbers
        continue
        # Print odd numbers
    print(num)
print("End")