# Name:         Set Methods(05_Set_Methods.py)
# Purpose:      To Demonstrate various set methods.
# Author:       LF
# Created:      08-April-2025
# Updated:      08-April-2025
#-----------------------------------------------------------------------------

print("Start")
#Printing a set and naming it data
data = {10, 20, 30, 40, 50}
#Copy the set to `data_copy` and print it
data_copy = data.copy()
print(data_copy)
#Use `.pop()` to remove a random element and print the set
data.pop()
print("After pop:", data)
#Use `.clear()` to empty the set and print it
data.clear()
print("After clear:", data)
print("End")