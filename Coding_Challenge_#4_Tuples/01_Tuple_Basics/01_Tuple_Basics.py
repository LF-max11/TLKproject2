#-----------------------------------------------------------------------------
# Name:         Tuple Basics(01_Tuple_Basics.py)
# Purpose:      To Create a tuple with five different elements, including an integer,
#               a float, a string, a boolean, and another tuple
# Author:       LF
# Created:      28-March-2025
# Updated:      28-March-2025
#-----------------------------------------------------------------------------

print("Start")
# First Creating the tuple with five different elements
my_tuple = (20, 5.5,'Hello', True, (4,5,6)  )
# Second Print the entire tuple
print(my_tuple)
# Third Access and print the third element
print(my_tuple[2])
# Fourth Extract the nested tuple
nested_tuple = (my_tuple[4])
# Print the nested tuple
print(nested_tuple)
# Print the first element of nested tuple
print(nested_tuple[0])
print("End")
