#-----------------------------------------------------------------------------
# Name:         Tuple Operations and Count(03_ Tuple_Operations_and_Count.py)
# Purpose:      Create a tuple with repeated values
# Author:       LF
# Created:      1-April-2025
# Updated:      1-April-2025
#-----------------------------------------------------------------------------

print("Start")
# Create a tuple with repeated values
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")
# Ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")
# Print how many times the entered fruit appears in the tuple
fruit_count = fruit_tuple.count(fruit_name)
# Display the result
print(f"'{fruit_name}' appears {fruit_count} times in the tuple.")
print("End")