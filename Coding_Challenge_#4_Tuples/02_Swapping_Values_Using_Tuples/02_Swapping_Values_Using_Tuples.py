#-----------------------------------------------------------------------------
# Name:         Swapping Values Using Tuples(02_Swapping_Values_Using_Tuples.py)
# Purpose:      To tuple unpacking is to allow swapping values
#               between variables without needing a temporary variable.
# Author:       LF
# Created:      28-March-2025
# Updated:      28-March-2025
#-----------------------------------------------------------------------------

print("Start")
# Ask the user to input the first number
First_number = int(input("Enter a Number: "))
# Ask the user to input the second number
Second_number = int(input("Enter another Number: "))
# Store both numbers in a tuple and print it
numbers = (First_number, Second_number)
print(numbers)
# Swap the values of the two numbers using tuple unpacking
First_number, Second_number = Second_number, First_number
# Print the swapped values
print(First_number, Second_number)
print("End")